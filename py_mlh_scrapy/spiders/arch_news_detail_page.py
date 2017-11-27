from scrapy_redis.spiders import RedisSpider

from py_mlh_scrapy.helper.chineseDateUtil import ChineseDateUtil
from py_mlh_scrapy.items import DetailItem, ImageItem

"""
    class name represent the collection name in mongodb
    author:kaishui
"""


class arch_news_detail_page(RedisSpider):
    name = "arch_news_detail_page"

    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy_redis.pipelines.RedisPipeline': 298,
            'py_mlh_scrapy.pipelines_detail.PipelineDetail': 299,
            'py_mlh_scrapy.pipelines_detail_convert_to_news.ConvertToNews': 300
        }
    }

    def start_requests(self):
        # 设置redis start urls 参考：scrapy_max_picture_page_start_urls_spider
        return super().next_requests()

    # 详情页面
    def parse(self, response):
        detail = DetailItem()
        # 来源
        detail['url'] = response.url
        # 标题
        detail["title"] = response.xpath('//*[@id="content"]/div/div[3]/header/h1/text()').extract_first().strip()
        # createUser
        detail["createUser"] = response.xpath('//*[@id="single-meta"]/li[2]/a/strong/text()').extract_first()
        # 发布时间
        self.getTime(detail, response)
        # 获取图片
        self.getImgs(detail, response)
        # 类型
        detail['type'] = response.xpath('//header/ol/li[2]/a/span/text()').extract_first().strip()
        self.getDetail(detail, response)
        yield detail

    # createTime
    def getTime(self, detail, response):
        createTime = response.xpath('//*[@id="single-meta"]/li[1]/text()').extract_first().strip()
        detail["createTime"] = ChineseDateUtil.strToDate(createTime)

    # content
    def getDetail(self, detail, response):
        # 内容
        contents = response.xpath('//*[@id="single-content"]/p/text()|//*[@id="single-content"]/p/a/text()').extract()
        cts = []
        for content in contents:
            if content.strip() != "":
                cts.append(content.strip())
        detail['content'] = cts

    # 获取图片
    def getImgs(self, detail, response):
        imgsLis = response.xpath('//article[@id="single-content"]//img')
        imgs = []
        for imgLi in imgsLis:
            img = ImageItem()
            # 版权信息
            img["copyright"] = imgLi.xpath('./@src').extract_first()
            # 图片uri
            img["origin"] = imgLi.xpath('./@alt').extract_first()
            # 操作
            img["op"] = "act"
            imgs.append(dict(img))
        detail['originImgs'] = imgs
