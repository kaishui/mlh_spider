# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import time

from py_mlh_scrapy.helper.mongo_util import MongoSupport
from py_mlh_scrapy.helper.static_config import StaticConfig


class ConvertToNews(object):

    def __init__(self, mongoclient):
        self.mongoclient = mongoclient

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongoclient= MongoSupport()
        )

    def open_spider(self, spider):
        logging.debug("open_spider....")

    def close_spider(self, spider):
        logging.debug("close_spider....")

    # save news
    def process_item(self, item, spider):
        # 方法名是collection name
        collectionName =StaticConfig().news
        logging.debug("spider name: %s -- %s", spider.name, collectionName)
        detail = dict(item)

        news = dict()
        news["_id"] = self.mongoclient.get_mongo_id()
        news["content"] = "".join(detail["content"])
        news["createTime"] = int(round(time.time() * 1000))
        news["realTime"] = int(detail["createTime"])
        news["sourceUrl"] = detail["url"]
        news["title"] = detail["title"]
        news["site"] = "ArchDaily"
        news["sourceWebsite"] = "ArchDaily"
        news["op"] = "ACT"
        news["type"] = "project"
        # 插入db
        id = self.mongoclient.db[collectionName].insert(news)
        logging.debug("news id : %s", id)
        return item