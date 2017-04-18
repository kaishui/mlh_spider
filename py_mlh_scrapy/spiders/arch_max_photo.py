import scrapy

from py_mlh_scrapy.items import ImageItem

from urllib.parse import urlparse

"""
    class name represent the collection name in mongodb
    author:kaishui
"""


class scrapy_max_photo(scrapy.Spider):
    name = "arch_max_photo_spider"

    # 用户自定义setting 参考settings
    custom_settings = {
        "ITEM_PIPELINES": {
            'py_mlh_scrapy.pipelines_update_max_photo.UpdateMaxPhotoPipeline': 300,
            'py_mlh_scrapy.pipelines_downloader_photo.DownloaderPhotoPipeline':301
        }
    }

    # 从mongodb 获取需要爬取的url
    def start_requests(self):
        # mongoclient = MongoSupport()
        # collection = mongoclient.db["scrapy_urls"]
        # urls = collection.find({}, projection={"uri": 1, "_id": 0}, limit=2)
        # TODO get source photo
        urls = ["/cn/803258/xiang-shu-wu-gao-ji-zhong-xue-da-lou-trasbordo-arquitectura/585c993ce58ece953e000308-edificio-de-bachillerato-oak-house-school-trasbordo-arquitectura-photo"]
        baseUrl = "http://www.archdaily.cn"
        for uri in urls:
            print("uri : %s", uri)
            yield scrapy.Request(url=baseUrl + uri, callback=self.parse_photo)

    # 图片详情页面
    def parse_photo(self, response):
        imgItem = ImageItem()
        url =  urlparse(response.url)
        # 来源
        imgItem['origin'] = url.path
        # 原图
        imgItem["target"] = response.xpath('//meta[@property="og:image"]/@content').extract_first().strip()

        yield imgItem
