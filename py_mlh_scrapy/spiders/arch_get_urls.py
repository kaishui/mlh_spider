"""
爬取archdaily 项目： http://www.archdaily.cn/cn/search/projects
author:kaishui
"""
import logging
import scrapy as scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from py_mlh_scrapy.helper.mongo_util import MongoSupport
from py_mlh_scrapy.helper.static_config import StaticConfig
from py_mlh_scrapy.items import ListItem

from py_mlh_scrapy.spiders.arch_get_detail import scrapy_detail
from py_mlh_scrapy.spiders.arch_max_photo import scrapy_max_photo
from py_mlh_scrapy.spiders.arch_max_photo_page_redis import scrapy_max_picture_page_spider
from py_mlh_scrapy.spiders.arch_max_photo_page_start_urls import scrapy_max_picture_page_start_urls_spider
from py_mlh_scrapy.spiders.arch_for_demo import scrapy_max_picture_page


class scrapy_urls(scrapy.Spider):
    # 爬虫名称
    name = "scrapy_urls"

    # setting for this spider
    custom_settings = {
        "ITEM_PIPELINES": {
            # 'py_mlh_scrapy.pipelines_save_urls_redis.UrlsRedisPipeline': 299,
            'py_mlh_scrapy.pipelines_save_urls.UrlsPipeline': 300
        }
    }

    def __init__(self, name=None, **kwargs):
        super(scrapy_urls, self).__init__(name, **kwargs)
        self.baseUrl = "https://www.archdaily.cn/cn/search/projects?page="
        self.page = 0
        self.maxPage = 0
        self.mongoclient = MongoSupport()

    def start_requests(self):
        self.page += 1
        yield scrapy.Request(self.baseUrl + str(self.page), dont_filter=True,
                             callback=self.parse_page)

    def parse_page(self, response):
        if self.maxPage == 0:
            # follow pagination 获取最后一页
            self.maxPage = int(response.xpath('//*[@id="pagination_container"]/div/div/a[6]/@href').re(r'(\d+)')[0])

        item = ListItem()
        # uri
        item['url'] = response.xpath(
            '//div[@id="search-results"]/div/ul/li/a[@class="afd-search-list__link"]/@href').extract()
        # 标题
        item['title'] = response.xpath('//div[@id="search-results"]/div/ul/li/a/h2/text()').extract()
        item['site'] = "archdaily"
        self.logger.info("url %s", item)

        # 在数据库中查询，是否已经存在uri，如果存在循环结束

        existUriCount = self.mongoclient.db[StaticConfig().archContentUrls].find({"uri": {"$in": item["url"]}}).count()
        yield item
        if self.page <= self.maxPage and existUriCount == 0:
            self.page += 1
            yield scrapy.Request(self.baseUrl + str(self.page), dont_filter=True,
                                 callback=self.parse_page)
        else:
            logging.debug("%s 有重复数据", response.url)


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    # # # 加入爬虫
    # process.crawl(scrapy_urls)
    process.crawl(scrapy_detail)
    # # process.crawl(scrapy_max_photo)
    # # process.crawl(scrapy_max_demo)
    # process.crawl(scrapy_max_picture_page_spider)
    # process.crawl(scrapy_max_picture_page)
    # # process.crawl(scrapy_max_picture_page_start_urls_spider)
    process.start()
