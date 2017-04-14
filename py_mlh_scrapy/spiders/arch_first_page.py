"""
爬取archdaily 项目： http://www.archdaily.cn/cn/search/projects
author:kaishui
"""
import scrapy as scrapy

from py_mlh_scrapy.items import ListItem


class archdailyProjectListSpider(scrapy.Spider):
    # 爬虫名称
    name = "ad_project_list"

    # setting for this spider
    custom_settings = {
        "ITEM_PIPELINES" : {
            'py_mlh_scrapy.pipelines_first.MongodbFirstPipeline': 300
        }
    }

    # 开始Url
    start_urls = [
        "http://www.archdaily.cn/cn/search/projects?page=1",
    ]

    def parse(self, response):
        # projects = response.xpath('//*[@class="afd-search-list__item"]')
        # self.logger.info("projects list: %s", projects.extract_first())
        item = ListItem()
        item['url'] = response.xpath('//div[@id="search-results"]/div/ul/li/a[@class="afd-search-list__link"]/@href').extract()
        item['title'] = response.xpath('//div[@id="search-results"]/div/ul/li/a/h2/text()').extract()

        # self.logger.info("url %s", item)
        yield item


# process = CrawlerProcess(get_project_settings())
#
# process.crawl(archdailyProjectListSpider)
# process.start()