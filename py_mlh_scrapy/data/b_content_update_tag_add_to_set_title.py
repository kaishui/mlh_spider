import logging

from py_mlh_scrapy.helper.mongo_util import MongoSupport


class data_to_dev(object):

    testMongo = MongoSupport()

    def testToDev(self):
        testCount = self.testMongo.db["b_content"].count({"isDeal": {"$exists": 0}, "sourceWebsite" : "archdaily","type":"product"});
        skip = 0;

        while skip < testCount:
            skip += 500;
            # 获取爬虫详情数据数据
            details = self.testMongo.db['b_content'].aggregate(
                [
                    {"$match": {"isDeal": {"$exists": 0}, "sourceWebsite" : "archdaily","type":"product"}},
                    {"$sort": {"_id": -1}},
                    {"$skip": 0},
                    {"$limit": 500}
                ]
            )
            for sdetail in details:
                logging.debug(sdetail)
                # 更新项目信息
                self.testMongo.db['b_content'].update({"_id": sdetail["_id"]}, { "$addToSet": {"tag": { "$each": sdetail["title"]}}})

                # 标志这条爬虫数据已经处理过
                self.testMongo.db['b_content'].update({"_id": sdetail["_id"]}, {"$set": {"isDeal": "Y"}});

if __name__ == '__main__':
    data_to_dev().testToDev()