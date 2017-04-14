# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging

from bson.objectid import ObjectId

from py_mlh_scrapy.helper.mongoclient import MongoClient


class MongodbDeptPipeline(object):

    def __init__(self, mongoclient):
        self.mongoclient = mongoclient

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongoclient= MongoClient()
        )

    def open_spider(self, spider):
        logging.debug("open_spider....")

    def close_spider(self, spider):
        logging.debug("close_spider....")

    def process_item(self, item, spider):
        collectionName = spider.__class__.__name__
        logging.debug("spider name: %s -- %s", spider.name, collectionName)
        id = self.mongoclient.db[collectionName].insert(dict(item))
        logging.debug("id type :", id)
        project = self.mongoclient.db[collectionName].find_one({"_id", str(id)})
        return item