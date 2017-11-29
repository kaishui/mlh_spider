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
from py_mlh_scrapy.spiders.arch_news_detail_page import arch_news_detail_page

from py_mlh_scrapy.spiders.arch_get_detail_projects import arch_project_detail
from py_mlh_scrapy.spiders.arch_max_photo import scrapy_max_photo
from py_mlh_scrapy.spiders.arch_max_photo_page_redis import scrapy_max_picture_page_spider
from py_mlh_scrapy.spiders.arch_max_photo_page_start_urls import scrapy_max_picture_page_start_urls_spider
from py_mlh_scrapy.spiders.arch_for_demo import scrapy_max_picture_page
from py_mlh_scrapy.spiders.arch_news_detail_page_start_urls import scrapy_news_detail_start_urls_spider


class arch_news_list(scrapy.Spider, MongoSupport):
    # 爬虫名称
    name = "arch_news_list"

    # setting for this spider
    custom_settings = {
        "ITEM_PIPELINES": {
            # 'py_mlh_scrapy.pipelines_save_urls_redis.UrlsRedisPipeline': 299,
            'py_mlh_scrapy.pipelines_save_urls.UrlsPipeline': 300
        }
    }

    @classmethod
    def from_crawler(self, crawler, *args, **kwargs):
        obj = super(arch_news_list, self).from_crawler(crawler, *args, **kwargs)
        obj.set_mongo_client(crawler)
        return obj

    def __init__(self, page="0", duplicate=False, name=None, **kwargs):
        super(arch_news_list, self).__init__(name, **kwargs)
        self.baseUrl = "https://www.archdaily.cn/cn/xin-wen/page/"
        self.page = int(page)
        self.maxPage = 0
        self.duplicate = duplicate

    def start_requests(self):
        self.page += 1
        yield scrapy.Request(self.baseUrl + str(self.page), dont_filter=True,
                             callback=self.parse_page)

    def parse_page(self, response):
        if self.maxPage == 0:
            # follow pagination 获取最后一页
            self.maxPage = int(response.xpath('//div[@class="pagination"]//a[@class="last"]/@href').re(r'(\d+)')[0])

        item = ListItem()
        # uri
        item['url'] = response.xpath('//div[@id="main"]/div[1]/div/h3/a/@href').extract()
        # 标题
        item['title'] = response.xpath(' //div[@id="main"]/div[1]/div/h3/a/span/text()').extract()
        item['site'] = "archdaily_news"
        self.logger.info("url %s", item)

        # 在数据库中查询，是否已经存在uri，如果存在循环结束

        existUriCount = self.db[StaticConfig().archContentUrls].find({"uri": {"$in": item["url"]}}).count()
        yield item
        if  self.page <= self.maxPage and (existUriCount == 0 or self.duplicate):
            self.page += 1
            yield scrapy.Request(self.baseUrl + str(self.page), dont_filter=True,
                                 callback=self.parse_page)
        else:
            logging.debug("%s 有重复数据: %d", response.url, existUriCount)


# if __name__ == '__main__':
#     process = CrawlerProcess(get_project_settings())
#     # # # 加入爬虫
#     process.crawl(arch_news_list, duplicate=True)
#     # process.crawl(scrapy_news_detail_start_urls_spider, site="archdaily_news", detail_spider="arch_news_detail_page")
#     # process.crawl(scrapy_news_detail_start_urls_spider, site="archdaily", detail_spider="arch_project_detail")
#     # process.crawl(arch_news_detail_page)
#     # process.crawl(arch_project_detail)
#     # # process.crawl(scrapy_max_photo)
#     # # process.crawl(scrapy_max_demo)
#     # process.crawl(scrapy_max_picture_page_spider)
#     # process.crawl(scrapy_max_picture_page)
#     process.crawl(scrapy_max_picture_page_start_urls_spider)
#     process.start()
