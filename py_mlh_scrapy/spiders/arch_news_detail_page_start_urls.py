import logging

from scrapy_redis.spiders import RedisSpider

from py_mlh_scrapy.helper.mongo_util import MongoSupport
# 把urls放入redis start_urls中
from py_mlh_scrapy.helper.static_config import StaticConfig


class scrapy_news_detail_start_urls_spider(RedisSpider, MongoSupport):
    name = "scrapy_news_detail_start_urls_spider"
    mongoclient = None

    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy_redis.pipelines.RedisPipeline': 298
        }
    }

    def __init__(self, **kwargs):
        super(scrapy_news_detail_start_urls_spider, self).__init__(name=self.name, **kwargs)

        self.site = kwargs.get("site")
        self.detail_spider = kwargs.get("detail_spider")

    @classmethod
    def from_crawler(self,crawler, *args, **kwargs):
        obj = super(scrapy_news_detail_start_urls_spider, self).from_crawler(crawler, *args, **kwargs)
        obj.set_mongo_client(crawler)
        return obj


    # 从mongodb 获取需要爬取的url
    def start_requests(self):
        collection = self.db[StaticConfig().archContentUrls]
        # GET SUM NUMBER
        count = collection.count({"op": "ACT", "uri": {"$exists": 1}, "site": self.site})
        skip = 0
        limit = 500
        while skip < count:
            urls = collection.find({"op": "ACT", "uri": {"$exists": 1}, "site": self.site},
                                   projection={"uri": 1, "_id": 1}).skip(skip).limit(limit)
            baseUrl = StaticConfig().arch
            ids = []
            for uri in urls:
                # extract ids
                ids.append(uri["_id"])
                logging.debug("uri : %s", uri["uri"])
                self.server.rpush(self.detail_spider + ":start_urls", baseUrl + uri["uri"])
            # update items have scraped
            collection.update_many({"_id": {"$in": ids}}, {"$set": {"op": "SCRAPY"}}, upsert=True)
            skip += limit
        return None
