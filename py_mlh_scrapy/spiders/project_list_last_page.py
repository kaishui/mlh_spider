import logging

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from py_mlh_scrapy.items import listItem


class archdailySpider(scrapy.Spider):
    name = "archdaily"
    start_urls = [
        "http://www.archdaily.cn/cn/search/projects"
    ]

    custom_settings = {
        "ITEM_PIPELINES": {
            'py_mlh_scrapy.pipelines_last.MongodbUrlsPipeline': 400
        }
    }

    def parse(self, response):
        # follow pagination 获取最后一页
        num_pages = int(response.xpath('//*[@id="pagination_container"]/div/div/a[6]/@href').re(r'(\d+)')[0])

        base_url = 'http://www.archdaily.cn/cn/search/projects?page='
        for page in range(1, num_pages + 1):
            logging.debug("page num: %s", page)
            # 遍历每一页查找所有项目的url
            yield scrapy.Request(base_url + str(page), dont_filter=True,
                                 callback=self.parse_page)

    # 提取每个项目的 title & uri
    def parse_page(self, response):
        item = listItem()
        item['url'] = response.xpath(
            '//div[@id="search-results"]/div/ul/li/a[@class="afd-search-list__link"]/@href').extract()
        item['title'] = response.xpath('//div[@id="search-results"]/div/ul/li/a/h2/text()').extract()

        # self.logger.info("url %s", item)
        yield item


process = CrawlerProcess(get_project_settings())

process.crawl(archdailySpider)
process.start()
