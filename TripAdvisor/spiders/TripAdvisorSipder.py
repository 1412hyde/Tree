# -*- coding: utf-8 -*-
import re
import sys
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from TripAdvisor.items import TripadvisorForumItem
from TripAdvisor.items import TripadvisorUserItem

# Python codes with utf-8
reload(sys)
sys.setdefaultencoding('utf8')

class TripaAdvisorSpider(Spider):
    name = "TripAdvisorSpider"

    # download_delay = 0.5
    allowed_domains = ["tripadvisor.com"]
    start_urls = [
        "https://www.tripadvisor.com/ShowForum-g186338-i17-London_England.html"
    ]

    def parse(self, response):

        # forum list
        sel = Selector(response)

        # search topics in current page
        item_urls = sel.xpath('//table[@id = "SHOW_FORUMS_TABLE"]/tr/td[2]/b/a/@href').extract()

        # Access each topic page
        for item_url in item_urls:
            item_url = "https://www.tripadvisor.com" + item_url
            yield Request(item_url,callback=self.parse_forum_topic)



    def parse_forum_topic(self,response):

        # forum topic
        sel = Selector(response)
        item = TripadvisorForumItem()
        # print response.url
        url = response.url
        pattern_url = re.compile('https://www.tripadvisor.com/ShowTopic-(.*?)-(.*?)-(.*?)-(.*?)-(.*?).html')
        re_items = re.findall(pattern_url,url)
        for re_item in re_items:
            # print reitem[0],reitem[2],reitem[3],reitem[4]
            item['forum_topic_id'] = re_item[2]
            item['forum_locate_id'] = re_item[0]

        item['forum_topic_url'] = response.url
        item['forum_topic_name'] = sel.xpath('//h1[@id="HEADING"]/text()').extract()
        item['forum_topic_author'] = sel.xpath('//div[@id="SHOW_TOPIC"]/div[1]/div[6]/div/div/div[1]/div[2]/a/span/text()').extract()
        item['forum_topic_time'] = sel.xpath('//div[@id="SHOW_TOPIC"]/div[1]/div[6]/div/div/div[2]/div[1]/div[2]/text()').extract()
        item['forum_topic_text'] = sel.xpath('//div[@id="SHOW_TOPIC"]/div[1]/div[6]/div/div/div[2]/div[1]/div[3]/p/text()').extract()
        yield item

        # Access the page of User's Information
        urls = sel.xpath('//div[@id="SHOW_TOPIC"]/div[1]/div[6]/div/div/div[1]/div[2]/a/@href').extract()
        for url in urls:
            url = "https://www.tripadvisor.com" + url
            yield Request(url,callback=self.parse_forum_userInfo)

    def parse_forum_userInfo(self,response):

        # forum userInfo
        sel = Selector(response)
        item = TripadvisorUserItem()
        # print response.url,"    In func-User-Info"
        item['user_name'] = sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]/div[1]/div[1]/div[1]/div/div[@class= "name"]/span/text()').extract()
        # print item['user_name'],"   In func-User-Info"
        item['user_registerDate'] = sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]/div[1]/div[1]/div[@class="profInfo"]/div[@class="ageSince"]/p[@class="since"]/text()').extract()
        item['user_ageSex'] = sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]/div[1]/div[1]/div[@class="profInfo"]/div[@class="ageSince"]/p[2]/text()').extract()
        item['user_Position'] = sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]/div[1]/div[1]/div[@class="profInfo"]/div[@class="hometown"]/p/text()').extract()
        item['user_ReviewCnt'] = sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]/div[1]/div[2]/div/ul/li[@class="content-info"]/a[@name="reviews"]/text()').extract()
        item['user_ForumPostCnt'] = sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]/div[1]/div[2]/div/ul/li[@class="content-info"]/a[@name="forums"]/text()').extract()
        item['user_tags'] = sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]/div[1]/div[4]/div/div[@class="tagBlock"]/div/text()').extract()
        item['user_Point'] = sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]/div[2]/div[2]/div[1]/div/div[@class="points"]/text()').extract()
        yield item