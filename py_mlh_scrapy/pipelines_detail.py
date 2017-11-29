# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging

from py_mlh_scrapy.helper.mongo_util import MongoSupport
from py_mlh_scrapy.helper.static_config import StaticConfig


class PipelineDetail(object):

    def __init__(self, mongoclient):
        self.mongoclient = mongoclient

    @classmethod
    def from_crawler(cls, crawler):
        mongoclient = MongoSupport(crawler)
        return cls(mongoclient)

    def open_spider(self, spider):
        logging.debug("open_spider....")

    def close_spider(self, spider):
        logging.debug("close_spider....")

    # save 详情页面元素
    def process_item(self, item, spider):
        # 方法名是collection name
        collectionName =StaticConfig().archContents
        logging.debug("spider name: %s -- %s", spider.name, collectionName)
        detail = dict(item)
        detail["_id"] = self.mongoclient.get_mongo_id()
        # 插入db
        id = self.mongoclient.db[collectionName].insert(detail)
        logging.debug("id type :", id)
        return item