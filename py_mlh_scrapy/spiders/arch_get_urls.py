"""
爬取archdaily 项目： http://www.archdaily.cn/cn/search/projects
author:kaishui
"""
import scrapy as scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from py_mlh_scrapy.items import ListItem

from py_mlh_scrapy.spiders.arch_get_detail import scrapy_detail

class scrapy_urls(scrapy.Spider):
    # 爬虫名称
    name = "scrapy_urls"

    # setting for this spider
    custom_settings = {
        "ITEM_PIPELINES" : {
            'py_mlh_scrapy.pipelines_save_urls.UrlsPipeline': 300
        }
    }

    # 开始Url
    start_urls = [
        "http://www.archdaily.cn/cn/search/projects?page=1",
    ]

    def parse(self, response):
        item = ListItem()
        # uri
        item['url'] = response.xpath('//div[@id="search-results"]/div/ul/li/a[@class="afd-search-list__link"]/@href').extract()
        # 标题
        item['title'] = response.xpath('//div[@id="search-results"]/div/ul/li/a/h2/text()').extract()
        # self.logger.info("url %s", item)
        yield item


process = CrawlerProcess(get_project_settings())
# 加入爬虫
process.crawl(scrapy_urls)
# process.crawl(scrapy_detail)
process.start()