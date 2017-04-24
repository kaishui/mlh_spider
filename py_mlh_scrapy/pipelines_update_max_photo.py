# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging

from py_mlh_scrapy.helper.mongo_util import MongoSupport

# 更新图片url
class UpdateMaxPhotoPipeline(object):
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

    # 更新最大图片信息
    def process_item(self, item, spider):
        logging.debug("spider name: %s", spider.name)
        collectionName = "scrapy_detail"
        logging.debug("spider name: %s -- %s", spider.name, collectionName)
        # 查询条件
        query = {"originImgs.origin": item['origin']}
        updateField = {}
        # 原图url
        if item['target']:
            updateField["originImgs.$.target"] = item['target']
        # oss 中的id
        if item['ossImgUrl']:
            updateField["originImgs.$.ossImgUrl"] = item['ossImgUrl']
        #  本地地址
        if item['localImgUrl']:
            updateField["originImgs.$.localImgUrl"] = item['localImgUrl']
        # 更新最大图片
        update = {"$set" : updateField}
        updateResult = self.mongoclient.db[collectionName].update(query, update, multi=True)
        logging.debug("update mongo result %s", str(updateResult))
        return item
