# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy_redis.pipelines import RedisPipeline

# 保存大图片链接进入redis,给
class MaxPicturePageUrlsRedisPipeline(RedisPipeline):

    # 重载redis _process_item
    def _process_item(self, item, spider):
        # get redis key
        key = self.item_key(item, spider)
        url = item["target"]
        # rpush into redis
        self.server.rpush(key, url)
        return item

    # 保存给下一个redis spider 的start urls 格式：%(name)s:start_urls
    def item_key(self, item, spider):
        """Returns redis key based on given spider.

        Override this function to use a different key depending on the item
        and/or spider.

        """
        return self.key % {'spider': spider.name}