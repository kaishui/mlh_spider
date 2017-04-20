"""
爬取archdaily 项目： http://www.archdaily.cn/cn/search/projects
author:kaishui
"""
import logging
import scrapy as scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from py_mlh_scrapy.items import ListItem

from py_mlh_scrapy.spiders.arch_get_detail import scrapy_detail
from py_mlh_scrapy.spiders.arch_max_photo import scrapy_max_photo

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
        # follow pagination 获取最后一页
        num_pages = int(response.xpath('//*[@id="pagination_container"]/div/div/a[6]/@href').re(r'(\d+)')[0])

        base_url = 'http://www.archdaily.cn/cn/search/projects?page='
        for page in range(1, num_pages + 1):
        # for page in range(1, 2):
            logging.debug("page num: %s", page)
            # 遍历每一页查找所有项目的url
            yield scrapy.Request(base_url + str(page), dont_filter=True,
                                 callback=self.parse_page)

    def parse_page(self, response):
        item = ListItem()
        # uri
        item['url'] = response.xpath(
            '//div[@id="search-results"]/div/ul/li/a[@class="afd-search-list__link"]/@href').extract()
        # 标题
        item['title'] = response.xpath('//div[@id="search-results"]/div/ul/li/a/h2/text()').extract()
        item['site'] = "archdaily"
        # self.logger.info("url %s", item)
        yield item

# process = CrawlerProcess(get_project_settings())
# # 加入爬虫
# process.crawl(scrapy_urls)
# # process.crawl(scrapy_detail)
# # process.crawl(scrapy_max_photo)
# process.start()