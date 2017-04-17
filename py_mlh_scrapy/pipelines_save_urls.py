# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging

from bson import ObjectId

from py_mlh_scrapy.helper.mongo_util import MongoSupport


class UrlsPipeline(object):
    def __init__(self, mongoclient):
        self.mongoclient = mongoclient

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongoclient=MongoSupport()
        )

    def open_spider(self, spider):
        logging.debug("open_spider....")

    def close_spider(self, spider):
        logging.debug("close_spider....")

    # 存储 urls 列表页提取的uri
    def process_item(self, item, spider):
        logging.debug("spider name: %s", spider.name)
        collectionName = spider.__class__.__name__
        logging.debug("spider name: %s -- %s", spider.name, collectionName)
        if item is not None:
            # 每一页的列表uri
            projectList = []
            for index in range(len(item["url"])):
                url = item['url'][index]
                title = item['title'][index]
                logging.debug("item uri: %s -- %s", url, title)
                project = {"uri": url, "title": title, "site": item["site"], "op": "ACT", "_id": str(ObjectId())}
                projectList.append(project)
            self.db[collectionName].insert_many(projectList)
        return item
