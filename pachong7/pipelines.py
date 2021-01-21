# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo import MongoClient

class Pachong7Pipeline(object):

    def open_spider(self, spider):
        self.db = MongoClient('localhost', 27017).zhihu_db
        self.collection = self.db.zhihu_collection2

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))

    def close_spider(self, spider):
        self.collection.close()