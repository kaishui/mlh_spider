# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging

import pymongo

class MongodbFirstPipeline(object):
    collection_name = 'scrapy-project-urls'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_URI'),
            mongo_db=crawler.settings.get('MONGODB_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        logging.debug("spider name: %s", spider.name)
        if item is not None:
            projectList = []
            for index in range(len(item["url"])):
                url = item['url'][index]
                title = item['title'][index]
                logging.debug("item uri: %s -- %s", url, title)
                project = {"uri" : url, "title" : title}
                projectList.append(project)
            self.db[self.collection_name].insert_many(projectList)
        return item