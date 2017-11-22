import logging

from py_mlh_scrapy.helper.mongo_util import MongoSupport
from scrapy_redis.spiders import RedisSpider


# 把下载图片的页面放入redis start_urls中
from py_mlh_scrapy.helper.static_config import StaticConfig


class scrapy_max_picture_page_start_urls_spider(RedisSpider):
    name = "scrapy_max_picture_page_start_urls_spider"

    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy_redis.pipelines.RedisPipeline': 298,
        }
    }

    # 用户自定义setting 参考settings

    # 从mongodb 获取需要爬取的url
    def start_requests(self):
        mongoclient = MongoSupport()

        collection = mongoclient.db[StaticConfig().archContents]
        # 统计pipeline
        countPipeline = [
            {"$unwind": "$originImgs"},
            {"$match": {"originImgs.origin": {"$exists": True}, "originImgs.ossImgUrl": {"$exists": False}}},
            {"$project": {"origin": "$originImgs.origin", "_id": 0}},
            {"$group": {"_id": "null", "count": {"$sum": 1}}}
        ]
        # 统计条数
        countResult = collection.aggregate(countPipeline)

        baseUrl = StaticConfig().archContents
        # set redis
        # llen = self.server.llen
        # redisCount = llen(self.redis_key)
        # if not redisCount > 0:
        for cresult in countResult:
            count = cresult['count']
            skip = 0;
            while (skip < count):
                logging.debug("skip = ", skip, count)
                # 查询需要转换的url
                queryPipeline = [
                    {"$unwind": "$originImgs"},
                    {"$match": {"originImgs.origin": {"$exists": True},
                                "originImgs.ossImgUrl": {"$exists": False}}},
                    {"$project": {"origin": "$originImgs.origin", "_id": 0}},
                    {"$skip": skip},
                    {"$limit": 500}
                ]
                urls = collection.aggregate(queryPipeline)
                for index, uri in enumerate(urls):
                    maxUri = uri['origin']
                    if not maxUri.startswith(('http:', 'https:', 'ftp:')):
                        maxUri = baseUrl + maxUri
                    print("uri : %s", maxUri)
                    self.server.rpush("scrapy_max_picture_page_spider:start_urls", maxUri)
                    # yield scrapy.Request(url=baseUrl + uri['origin'], callback=lambda r:self.parse2(r, count, index))
                #  步进100
                skip += 500
        return None
