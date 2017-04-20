import scrapy

from py_mlh_scrapy.helper.mongo_util import MongoSupport
from py_mlh_scrapy.items import ImageItem

from urllib.parse import urlparse

"""
    class name represent the collection name in mongodb
    author:kaishui
"""

# 图片下载
class scrapy_max_photo(scrapy.Spider):
    name = "arch_max_photo_spider"

    # 用户自定义setting 参考settings
    custom_settings = {
        "ITEM_PIPELINES": {
            'py_mlh_scrapy.pipelines_update_max_photo.UpdateMaxPhotoPipeline': 300,
            'py_mlh_scrapy.pipelines_downloader_photo.DownloaderPhotoPipeline':299
        }
    }

    # 从mongodb 获取需要爬取的url
    def start_requests(self):
        mongoclient = MongoSupport()

        collection = mongoclient.db["scrapy_detail"]
        # 统计pipeline
        countPipeline = [
            {"$unwind": "$originImgs"},
            {"$match": {"originImgs.origin": {"$exists": True}, "originImgs.ossImgUrl": {"$exists": False}}},
            {"$project":{"origin" : "$originImgs.origin", "_id":0}},
            {"$group": {"_id": "null", "count": {"$sum": 1}}}
        ]
        # 统计条数
        countResult = collection.aggregate(countPipeline)

        baseUrl = "http://www.archdaily.cn"
        for cresult in countResult:
            count = cresult['count']
            skip = 0;
            while (skip < count):
                # 查询需要转换的url
                queryPipeline = [
                    {"$unwind": "$originImgs"},
                    {"$match": {"originImgs.origin": {"$exists": True}, "originImgs.ossImgUrl": {"$exists": False}}},
                    {"$project": {"origin": "$originImgs.origin", "_id": 0}},
                    {"$skip": skip},
                    {"$limit": 100}
                ]
                urls = collection.aggregate(queryPipeline)
                for uri in urls:
                    print("uri : %s", uri['origin'])
                    yield scrapy.Request(url=baseUrl + uri['origin'], callback=self.parse_photo)
                #  步进100
                skip += 100

    # 图片详情页面
    def parse_photo(self, response):
        imgItem = ImageItem()
        url =  urlparse(response.url)
        # 来源
        imgItem['origin'] = url.path
        # 原图
        imgItem["target"] = response.xpath('//meta[@property="og:image"]/@content').extract_first().strip()

        yield imgItem
