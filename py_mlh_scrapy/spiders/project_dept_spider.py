import logging

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from py_mlh_scrapy.items import DetailItem, Demension

"""
    class name represent the collection name in mongodb
"""
class scrapy_archdaily_detail(scrapy.Spider):
    name = "archdeptspider"
    start_urls = [
        "http://www.archdaily.cn/cn/search/projects"
    ]

    custom_settings = {
        "ITEM_PIPELINES": {
            'py_mlh_scrapy.pipelines_dept.MongodbDeptPipeline': 1
        }
    }

    def parse(self, response):
        # follow pagination 获取最后一页
        num_pages = int(response.xpath('//*[@id="pagination_container"]/div/div/a[6]/@href').re(r'(\d+)')[0])

        base_url = 'http://www.archdaily.cn/cn/search/projects?page='
        # for page in range(1, num_pages + 1):
        for page in range(1, 3):
            logging.debug("page num: %s", page)
            # 遍历每一页查找所有项目的url
            yield scrapy.Request(base_url + str(page), dont_filter=True,
                                 callback=self.parse_page)

    # 提取每个项目的uri
    def parse_page(self, response):
        for uri in response.xpath(
            '//div[@id="search-results"]/div/ul/li/a[@class="afd-search-list__link"]/@href').extract():
            uri = response.urljoin(uri)
            yield scrapy.Request(url = uri, callback=self.parse_detail)

    # 详情页面
    def parse_detail(self, response):
        detail = DetailItem()
        # 标题
        detail["title"] = response.xpath("//h1[@class='afd-title-big afd-title-big--bmargin-small afd-relativeposition']/text()")\
            .extract_first().strip()
        # 发布时间
        detail["createTime"] = response.xpath('//*[@id="single-meta"]/li[1]/text()').extract_first().strip()
        # 维度
        demensions = []
        vertors = response.xpath('//*[@id="single-content"]/ul/li')
        for d in vertors:
            logging.debug("demension : %s", d.extract())
            demension = Demension()
            demension['attr']= d.xpath("./h3/text()").extract_first()
            # 如果有链接就有内容，如果没有链接 if 部分
            text= d.xpath("./div/a/text()").extract_first()
            if text is None:
                text = d.xpath('./div/text()').extract_first()
            demension["text"] = text
            demensions.append(dict(demension))
        detail['category'] = demensions

        yield detail

process = CrawlerProcess(get_project_settings())

process.crawl(scrapy_archdaily_detail)
process.start()
