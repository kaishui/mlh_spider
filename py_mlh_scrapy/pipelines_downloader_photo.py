# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
import logging

import scrapy
from bson import ObjectId
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

# 下载图片
from py_mlh_scrapy.helper.aliyunoss import AliOss

# 下载图片到本地 并且上传到ALIYUN OSS
class DownloaderPhotoPipeline(ImagesPipeline):
    # aliyun oss client
    ossclient = AliOss()

    PHOTO_DIR = "/data/scrapy_download_photo/"


    def get_media_requests(self, item, info):
        yield scrapy.Request(item['target'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['localImgUrl'] = image_paths[0]

        # 时间搓 + objectId 当ID
        id = datetime.datetime.now().strftime("%Y%m%d%H%M%s") + str(ObjectId())
        logging.debug("id :", id)
        photoDir = self.PHOTO_DIR + item['localImgUrl']
        # 保存到 aliyun oss中 TODO 异步
        result = self.ossclient.bucket.put_object_from_file(id, photoDir)
        # oss 上传成功
        if 200 == result.status:
            item['ossImgUrl'] = id
        logging.debug("oss save result: ", result)
        return item

if __name__ == "__main__":
    # photoDir = "/data/scrapy_download_photo/full/6363f498c28fcca3ed77037750be168e5994e1a3.jpg"
    # with open(photoDir, mode="rb") as fileobj:
    #     print(fileobj)
    #     fileobj.close()

    print(datetime.datetime.now().strftime("%Y%m%d%H%M%s"))