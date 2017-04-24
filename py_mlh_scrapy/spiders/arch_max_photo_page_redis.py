import logging
from urllib.parse import urlparse

from py_mlh_scrapy.helper.mongo_util import MongoSupport
from py_mlh_scrapy.items import ImageItem
from scrapy_redis.spiders import RedisSpider

"""
    class name represent the collection name in mongodb
    author:kaishui
"""


# 图片下载
class scrapy_max_picture_page_spider(RedisSpider):
    name = "scrapy_max_picture_page_spider"

    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy_redis.pipelines.RedisPipeline': 298,
            'py_mlh_scrapy.pipelines_downloader_photo.DownloaderPhotoPipeline': 299,
            'py_mlh_scrapy.pipelines_update_max_photo.UpdateMaxPhotoPipeline': 300
        }
    }
    # 用户自定义setting 参考settings

    # 从mongodb 获取需要爬取的url
    def start_requests(self):
        # 设置redis start urls 参考：scrapy_max_picture_page_start_urls_spider
        return super().next_requests()

    # 大图片图片详情页面
    def parse(self, response):
        imgItem = ImageItem()
        url = urlparse(response.url)
        # 来源
        imgItem['origin'] = url.path
        # 原图
        imgItem["target"] = response.xpath('//meta[@property="og:image"]/@content').extract_first().strip()

        yield imgItem
