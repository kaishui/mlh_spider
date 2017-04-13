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
    title = Field(serializer=str)         # 标题
    originUrl = Field(serializer=str)     # 来源
    content = Field(serializer=str)       # 内容
    imgs = Field()          # 图片urls
    tags = Field()           # 标签
    createUser = Field(serializer=str)    # 作者
    createTime = Field(serializer=str)    # 创建时间
    category = Field()      # 分类


# 维度
class Demension(scrapy.Item):
    attr = Field(serializer=str)         # 属性
    text = Field(serializer=str)         # 值
