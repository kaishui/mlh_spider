import logging

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from py_mlh_scrapy.items import DetailItem, Demension

"""
    class name represent the collection name in mongodb
    author:kaishui
"""


class scrapy_archdaily_detail(scrapy.Spider):
    name = "archdeptspider"
    start_urls = [
        "http://www.archdaily.cn/cn/search/projects"
    ]

    # 用户自定义setting 参考settings
    custom_settings = {
        "ITEM_PIPELINES": {
            'py_mlh_scrapy.pipelines_dept.MongodbDeptPipeline': 1
        }
    }

    # 列表页面
    def parse(self, response):
        # follow pagination 获取最后一页
        num_pages = int(response.xpath('//*[@id="pagination_container"]/div/div/a[6]/@href').re(r'(\d+)')[0])

        base_url = 'http://www.archdaily.cn/cn/search/projects?page='
        # for page in range(1, num_pages + 1):
        for page in range(1, 2):
            logging.debug("page num: %s", page)
            # 遍历每一页查找所有项目的url
            yield scrapy.Request(base_url + str(page), dont_filter=True,
                                 callback=self.parse_page)

    # 提取每个项目的uri
    def parse_page(self, response):
        for uri in response.xpath(
                '//div[@id="search-results"]/div/ul/li/a[@class="afd-search-list__link"]/@href').extract():
            uri = response.urljoin(uri)
            # 爬取详情页面
            yield scrapy.Request(url=uri, callback=self.parse_detail)

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


        yield detail


    # 获取位置信息
    def getLocations(self, detail, response):
        locations = response.xpath('//div[@id="single-map"]')
        if locations is not None:
            # 维度
            latitude = locations.xpath('./a/@data-latitude').extract_first()
            # 经度
            longitude = locations.xpath('./a/@data-longitude').extract_first()
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


process = CrawlerProcess(get_project_settings())

process.crawl(scrapy_archdaily_detail)
process.start()
