import logging
import scrapy
from py_mlh_scrapy.helper.mongo_util import MongoSupport

from py_mlh_scrapy.helper.time_util import getCurTime

mongoclient = MongoSupport()

class scrapy_gooood(scrapy.Spider):




    name = "scrapy_goodhome"

    custom_settings={
        #检查是否重复策略采用默认值
        "DUPEFILTER_CLASS":"scrapy.dupefilter.RFPDupeFilter",
        "SCHEDULER" : "scrapy.core.scheduler.Scheduler"

    }

    def start_requests(self):
        #print("log is enabled! setting is",str(self.settings.attr['SCHEDULER']))
        url="http://www.gooood.hk/";
        #设置头部
        headers={"USER_AGENT":"Mediapartners-Google"};
        logging.info("begin to craw page",url)
        #
        yield scrapy.Request(url=url, callback=self.parse,headers=headers,dont_filter=True)

    def parse(self,res):

        pros=res.css(".post-wrapper")

        datas=[]
        for pro in pros:
            title=pro.css(".entry-title a::text").extract_first()
            des = pro.css(".post-excerpt a::text").extract_first();
            date = pro.css(".post-date::text").extract_first();
            url = pro.css(".entry-title a::attr('href')").extract_first();
            frontImage=pro.css(".post-thumbnail img::attr('src')").extract_first()
            data={"title":title,"content":des,"date":"realTime","sourceUrl":url,"frontImage":frontImage,
                  "op":"ACT","type":"project","sourceWebsite":"gooood","createTime":getCurTime(),
                  "site":"谷德设计网","_id":mongoclient.get_mongo_id()}

            #self.insertIfNotExist(data)
            datas.append(data)



        logging.info("datas is %s",datas)

    def insertIfNotExist(self,data):

        query={"title":data.get("title")}

        res = mongoclient.query_one("b_news",data)

        if not res :
            mongoclient.insert("b_news",data)





