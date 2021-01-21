# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Pachong7Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 名称
    name = scrapy.Field()
    # 介绍
    intro = scrapy.Field()
    # 详细资料
    detail = scrapy.Field()
    # 关注的对象数
    following = scrapy.Field()
    # 粉丝数
    followers = scrapy.Field()

