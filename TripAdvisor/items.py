# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class TripadvisorForumItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    forum_topic_id = Field()
    forum_locate_id = Field()
    forum_topic_name = Field()
    forum_topic_url = Field()
    forum_topic_author = Field()
    forum_topic_time = Field()
    forum_topic_text = Field()

class TripadvisorUserItem(Item):
    user_name = Field()
    user_registerDate = Field()
    user_ageSex = Field()
    user_Position = Field()
    user_ReviewCnt = Field()
    user_ForumPostCnt = Field()
    user_tags = Field()
    user_Point = Field()

    pass