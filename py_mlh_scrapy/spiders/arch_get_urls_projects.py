"""
爬取archdaily 项目： http://www.archdaily.cn/cn/search/projects
author:kaishui
"""
import logging

import scrapy as scrapy

from py_mlh_scrapy.helper.mongo_util import MongoSupport
from py_mlh_scrapy.helper.static_config import StaticConfig
from py_mlh_scrapy.items import ListItem


class arch_projects_list(scrapy.Spider, MongoSupport):
    # 爬虫名称
    name = "arch_projects_list"

    # setting for this spider
    custom_settings = {
        "ITEM_PIPELINES": {
            # 'py_mlh_scrapy.pipelines_save_urls_redis.UrlsRedisPipeline': 299,
            'py_mlh_scrapy.pipelines_save_urls.UrlsPipeline': 300
        }
    }

    @classmethod
    def from_crawler(self, crawler, *args, **kwargs):
        obj = super(arch_projects_list, self).from_crawler(crawler, *args, **kwargs)
        obj.set_mongo_client(crawler)
        return obj

    def __init__(self, page="0", duplicate=False, name=None, **kwargs):
        super(arch_projects_list, self).__init__(name, **kwargs)
        self.baseUrl = "https://www.archdaily.cn/cn/search/projects?page="
        self.page = int(page)
        self.maxPage = 0
        self.duplicate = duplicate
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

        existUriCount = self.db[StaticConfig().archContentUrls].find({"uri": {"$in": item["url"]}}).count()
        yield item
        if self.page <= self.maxPage and (existUriCount == 0 or self.duplicate):
            self.page += 1
            yield scrapy.Request(self.baseUrl + str(self.page), dont_filter=True,
                                 callback=self.parse_page)
        else:
            logging.debug("%s 有重复数据: %d", response.url, existUriCount)
