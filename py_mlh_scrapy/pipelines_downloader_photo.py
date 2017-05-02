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
from twisted.internet.threads import deferToThread

from py_mlh_scrapy.helper.aliyunoss import AliOss


# 下载图片到本地 并且上传到ALIYUN OSS
class DownloaderPhotoPipeline(ImagesPipeline):
    # aliyun oss client
    ossclient = AliOss()

    # images store
    # PHOTO_DIR = store_uri

    # 图片文件夹路径
    # TODO: GET FROM SETTINGS
    def getPhotoPath(self):
        return "/opt/spider/scrapy_download_photo/"

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['target'])

    # 下载完成
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['localImgUrl'] = image_paths[0]
        # 上传到oss
        return deferToThread(self._upload_to_alioss, item)

    # oss object key
    def getId(self):
        # 时间搓 + objectId 当ID
        id = datetime.datetime.now().strftime("%Y%m%d%H%M%s") + str(ObjectId())
        logging.debug("id :", id)
        return id

    # 上传到oss
    def _upload_to_alioss(self, item):
        item['ossImgUrl'] = self.getId()
        photoDir = self.getPhotoPath() + item['localImgUrl']
        # 保存到 aliyun oss中
        ossResult = self.ossclient.bucket.put_object_from_file(item['ossImgUrl'], photoDir)
        # oss 上传成功
        if 200 == ossResult.status:
            logging.debug("oss upload success '%s'", item['ossImgUrl'])
            return item
        else:
            logging.error("item: %s, oss result: %s", str(item), str(ossResult))
            raise DropItem("上传到OSS失败")