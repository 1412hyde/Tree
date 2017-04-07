# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting

import csv
# import json
import codecs

class TripadvisorPipeline(object):

    def __init__(self):
        # self.fileForum = file('data_1.csv','wb')
        # writerForum = csv.writer(self.file)
        # writer.writerow(['forum_topic_id','forum_locate_id','forum_topic_name','forum_topic_url','forum_topic_author','forum_locate_authorLocate','forum_topic_time','forum_topic_text'])

        self.fileForum = codecs.open('TripAdvisor_ForumData_Part_4.csv', mode='wb', encoding='utf-8')
        self.fileUserInfo = codecs.open('TripAdvisor_UserInfo_Part_4.csv', mode='wb', encoding='utf-8')
        line1 = csv.writer(self.fileForum)
        line2 = csv.writer(self.fileUserInfo)
        line1.writerow(['forum_topic_id','forum_topic_url','forum_topic_name','forum_topic_author','forum_topic_time','forum_locate_id','forum_topic_text'])
        line2.writerow(['user_name','user_registerDate','user_ageSex','user_Position','user_ReviewCnt','user_ForumPostCnt','user_tags','user_Point'])

    def process_item(self, item, spider):
        line1 = csv.writer(self.fileForum)
        line2 = csv.writer(self.fileUserInfo)

        if item.get('forum_topic_id'):
            line1.writerow((item.get('forum_topic_id'), item.get('forum_topic_url'),item.get('forum_topic_name'),item.get('forum_topic_author'),item.get('forum_topic_time'),item.get('forum_locate_id'),item.get('forum_topic_text')))


        elif item.get('user_name'):
            line2.writerow((item.get('user_name'), item.get('user_registerDate'),item.get('user_ageSex'),item.get('user_Position'),item.get('user_ReviewCnt'),item.get('user_ForumPostCnt'),item.get('user_tags'),item.get('user_Point')))


    def __del__(self):
        self.fileForum.close()
        self.fileUserInfo.close()
