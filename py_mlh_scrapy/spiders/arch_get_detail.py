import logging

import scrapy

from py_mlh_scrapy.helper.mongo_util import MongoSupport
from py_mlh_scrapy.items import DetailItem, Demension, ImageItem

"""
    class name represent the collection name in mongodb
    author:kaishui
"""


class scrapy_detail(scrapy.Spider):
    name = "archdeptspider"

    # 用户自定义setting 参考settings
    custom_settings = {
        "ITEM_PIPELINES": {
            'py_mlh_scrapy.pipelines_detail.PipelineDetail': 1
        }
    }

    # 从mongodb 获取需要爬取的url
    def start_requests(self):
        mongoclient = MongoSupport()
        collection = mongoclient.db["scrapy_urls"]
        urls = collection.find({}, projection={"uri": 1, "_id": 0})
        baseUrl = "http://www.archdaily.cn"
        for uri in urls:
            print("uri : %s", uri["uri"])
            yield scrapy.Request(url=baseUrl +  uri["uri"], callback=self.parse_detail)

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
        detail["createTime"] = response.xpath('//*[@id="single-meta"]/li[1]/text()').extract_first().strip()
        # 获取维度
        detail['category'] = self.getDemensions(response)
        # 标签
        detail['tags'] = response.xpath('//div[@class="single-tags-cats__module clearfix"]/a/text()').extract()
        # 获取位置信息
        self.getLocations(detail, response)
        # 获取图片
        self.getImgs(detail, response)
        # 类型
        detail['type'] = response.xpath('//div[@id="content"]/div/div[1]/header/ol/li[3]/a/span/text()').extract_first().strip()
        # 内容
        detail['content'] = response.xpath('//*[@id="single-content"]/p/text()').extract()
        yield detail

    # 获取图片
    def getImgs(self, detail, response):
        imgsLis = response.xpath('//ul[@id="gallery-thumbs"]/li')
        imgs = []
        for imgLi in imgsLis:
            img = ImageItem()
            # 版权信息
            img["copyright"] = imgLi.xpath('./span/text()').extract_first().strip()
            # 图片uri
            img["orgin"] = imgLi.xpath('./a/@href').extract_first().strip()
            # 操作
            img["op"] = "act"
            imgs.append(dict(img))
        detail['orginImgs'] = imgs

    # 获取位置信息
    def getLocations(self, detail, response):
        locations = response.xpath('//div[@id="single-map"]')
        if locations is not None:
            # 维度
            latitude = locations.xpath('./a/@data-latitude').extract_first()
            # 经度
            longitude = locations.xpath('./a/@data-longitude').extract_first()
            if latitude and longitude :
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
            demension['attr'] = d.xpath("./h3/text()").extract_first()
            # 如果有链接就有内容，如果没有链接 if 部分
            text = d.xpath("./div/a/text()").extract_first()
            if text is None:
                text = d.xpath('./div/text()').extract_first()
            demension["text"] = text
            demensions.append(dict(demension))
        return demensions