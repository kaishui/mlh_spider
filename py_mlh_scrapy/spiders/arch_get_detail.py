import logging

import scrapy

from py_mlh_scrapy.helper.chineseDateUtil import ChineseDateUtil
from py_mlh_scrapy.helper.mongo_util import MongoSupport
from py_mlh_scrapy.helper.static_config import StaticConfig
from py_mlh_scrapy.items import DetailItem, Demension, ImageItem

"""
    class name represent the collection name in mongodb
    author:kaishui
"""
class scrapy_detail(scrapy.Spider):
    name = "scrapy_detail"

    # 用户自定义setting 参考settings
    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy_redis.pipelines.RedisPipeline': 298,
            'py_mlh_scrapy.pipelines_detail.PipelineDetail': 299,
            'py_mlh_scrapy.pipelines_detail_convert_to_news.ConvertToNews': 300
        }
    }

    # 从mongodb 获取需要爬取的url
    def start_requests(self):
        mongoclient = MongoSupport()
        collection = mongoclient.db[StaticConfig().archContentUrls]
        # GET SUM NUMBER
        count = collection.count({"op": "ACT"})
        skip = 0
        limit = 100
        while (skip < count):
            urls = collection.find({"op": "ACT","uri":{"$exists": 1}}, projection={"uri": 1, "_id": 1}).skip(skip).limit(limit)
            baseUrl = StaticConfig().arch
            ids = []
            for uri in urls:
                #extract ids
                ids.append(uri["_id"])
                logging.debug("uri : %s", uri["uri"])
                yield scrapy.Request(url=baseUrl + uri["uri"], callback=self.parse_detail)
            # update items have scraped
            collection.update_many({"_id": {"$in": ids}}, {"$set": {"op": "SCRAPY"}}, upsert=True)
            skip += limit

    # 详情页面
    def parse_detail(self, response):
        detail = DetailItem()
        # 来源
        detail['url'] = response.url
        # 标题
        detail["title"] = response.xpath(
            "//h1[@class='afd-title-big afd-title-big--bmargin-small afd-relativeposition']/text()") \
            .extract_first().strip()
        # 发布时间
        self.getTime(detail, response)
        # 获取维度
        detail['category'] = self.getDemensions(response)
        # 标签
        detail['tags'] = response.xpath('//div[@class="single-tags-cats__module clearfix"]/a/text()').extract()
        # 获取位置信息
        self.getLocations(detail, response)
        # 获取图片
        self.getImgs(detail, response)
        # 类型
        detail['type'] = response.xpath('//header/ol/li[3]/a/span/text()').extract_first().strip()
        self.getDetail(detail, response)
        yield detail

    # createTime
    def getTime(self, detail, response):
        createTime = response.xpath('//*[@id="single-meta"]/li[1]/text()').extract_first().strip()
        detail["createTime"] = ChineseDateUtil.strToDate(createTime)

    # content
    def getDetail(self, detail, response):
        # 内容
        contents = response.xpath('//*[@id="single-content"]/p/text()').extract()
        cts = []
        for content in contents:
            if content.strip() != "":
                cts.append(content.strip())
        detail['content'] = cts

    # 获取图片
    def getImgs(self, detail, response):
        imgsLis = response.xpath('//ul[@id="gallery-thumbs"]/li')
        imgs = []
        for imgLi in imgsLis:
            img = ImageItem()
            # 版权信息
            img["copyright"] = imgLi.xpath('./span/text()').extract_first().strip()
            # 图片uri
            img["origin"] = imgLi.xpath('./a/@href').extract_first().strip()
            # 操作
            img["op"] = "act"
            imgs.append(dict(img))
        detail['originImgs'] = imgs

    # 获取位置信息
    def getLocations(self, detail, response):
        locations = response.xpath('//div[@id="single-map"]')
        if locations is not None:
            # 维度
            latitude = locations.xpath('./a/@data-latitude').extract_first()
            # 经度
            longitude = locations.xpath('./a/@data-longitude').extract_first()
            if latitude and longitude:
                address = dict({"latitude": latitude, "longitude": longitude})
                # 位置
                detail['location'] = address

    # 获取维度
    def getDemensions(self, response):
        # 维度
        demensions = []
        vertors = response.xpath('//*[@id="single-content"]/ul/li')
        for d in vertors:
            logging.debug("demension : %s", d.extract())
            demension = Demension()
            demension['attr'] = d.xpath("./h3/text()").extract_first().strip()
            # 如果有链接就有内容，如果没有链接 if 部分
            text = d.xpath("./div/a/text()").extract_first()
            if text is None:
                text = d.xpath('./div/text()').extract_first()
            demension["text"] = text.strip()
            demensions.append(dict(demension))
        return demensions
