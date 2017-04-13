# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy import Field


class ListItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    url = Field()


class DetailItem(scrapy.Item):
    # define the fields for your item here like:
    title = Field(serializer=str)           # 标题
    url = Field(serializer=str)             # 来源
    content = Field(serializer=str)         # 内容
    tags = Field()                          # 标签
    createUser = Field(serializer=str)      # 作者
    createTime = Field(serializer=str)      # 创建时间
    category = Field()                      # 分类
    location = Field()                      # 经维度 {""}
    orginImgs = Field()                     # 原图片 [{orgin:"image url", copyright："版权信息"}]
    targetImgs = Field()                    # 转化成目标图片urls [{orgin:"来源image url", target:"转化成阿里云oss url", copyright:"版权信息"}]


# 维度
class Demension(scrapy.Item):
    attr = Field(serializer=str)         # 属性
    text = Field(serializer=str)         # 值

# 图片信息
class ImgeItem(scrapy.Item):
    orgin = Field(serializer=str)       # 来源
    target = Field(serializer=str)      # 阿里云oss image url
    copyright = Field(serializer=str)   # 版权信息
