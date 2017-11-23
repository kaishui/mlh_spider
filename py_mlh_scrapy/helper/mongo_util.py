import logging
import pprint

from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient


# mongo client
class MongoSupport(object):
    '''
    classdocs
    '''
    db = None

    def __init__(self, mongo_url=None, mongo_dbname=None):
        '''
        :mongo_url 查询mongo数据库的连接字符串
        :mongo_dbname 要查询的数据库
        '''
        if self.db is None:
            if mongo_url is None:
                # dev env
                mongo_url = "mongodb://mlhtest:malianghang123@114.55.4.141:27017/mlh_dev?authMechanism=SCRAM-SHA-1"
                # mongo_url = "mongodb://mlhtest:malianghang123@114.55.4.141:27017/mlh_test?authMechanism=SCRAM-SHA-1"
            if mongo_dbname is None:
                mongo_dbname = "mlh_dev"
                # mongo_dbname = "mlh_test"

            self.client = MongoClient(mongo_url)

            self.db = self.client[mongo_dbname]

            logging.info("建立mongo连接:%s ,%s", mongo_url, mongo_dbname)

    def get_mongo_id(self):
        return str(ObjectId())

    def insert(self, collection_name, data):
        logging.debug("准备往表 :%s,插入记录：%s", collection_name, data)
        self.db[collection_name].insert(data)

    def query(self, collection_name, query, sort=None, limit=None, skip=None):
        '''
        :返回查询列表，不是普通的数组
        '''
        logging.debug("准备往表 :%s,查询记录：%s", collection_name, query)
        res = self.db[collection_name].find(query)

        if sort:
            res = res.sort(sort)
        if limit:
            res = res.limit(limit)
        if skip:
            res = res.skip(skip)
        return res

    def query_one(self, collection_name, query):
        '''
        :返回一个查询结果
        '''
        logging.debug("准备往表 :%s,查询记录：%s", collection_name, query)
        res = self.db[collection_name].find_one(query)

        return res

    def count(self, collection_name, query):
        '''
        :统计数量
        '''
        logging.debug("准备往表 :%s,统计数量：%s", collection_name, query)
        res = self.db[collection_name].count(query)
        return res

    def update(self, collection_name, update_query, update_object):
        '''
        :更新数据
        '''
        logging.debug("准备往表 :%s,更新数据：query:%s ,data:%s", collection_name, update_query, update_object)
        res = self.db[collection_name].update(update_query, update_object)
        return res


if __name__ == "__main__":
    mongoclient = MongoSupport()
    arr = []
    arr.append(dict({
        "_id": "5a166aa55a465c3ca1db5151",
        "uri": "/cn/884175/aesopyue-ke-gong-jue-yan-chang-dian-snohett2",
        "title": "Aesop约克公爵广场店 / Snøhetta",
        "site": "archdaily",
        "op": "ACT"
    }))

    arr.append(dict({
        "_id": "5a166aa55a465c3ca1db5152",
        "uri": "/cn/884175/aesopyue-ke-gong-jue-yan-chang-dian-snohetta",
        "title": "Aesop约克公爵广场店 / Snøhetta",
        "site": "archdaily",
        "op": "ACT"
    }))
    project = mongoclient.db['scrapy_archdaily_content_urls'].insert_many(arr)
    for value in project:
        print(value)
    pprint.pprint(project)
    print("mongclient")
