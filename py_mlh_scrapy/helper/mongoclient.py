import pymongo

"""
获取mongodb client
"""
class MongoClient(object):


    db = None
    __mongo_uri = "mongodb://mlhtest:malianghang123@114.55.4.141:27017/mlh_dev"
    __mongo_db = "mlh_dev"

    def __init__(self):
        super(MongoClient, self).__init__()
        self.db = None

    # mongodb client 单例
    def __new__(cls, *args, **kwargs):
        if cls.db is None:
            mongo_uri = cls.__mongo_uri
            mongo_db = cls.__mongo_db
            client = pymongo.MongoClient(mongo_uri)
            cls.db = client[mongo_db]
            return cls.db

if __name__ == "__main__":
    mongoclient = MongoClient()
    print("mongclient")