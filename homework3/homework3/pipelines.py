# -*- coding: utf-8 -*-
import json
import codecs
import sys
from scrapy import log
from sqlite3 import dbapi2 as sqlite
# Define your item pipelines here
#
from twisted.enterprise import adbapi
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Homework3Pipeline(object):

    def __init__(self):
        # Possible we should be doing this in spider_open instead, but okay
        self.dbpool = adbapi.ConnectionPool(
            "sqlite3", database="D:\homework3\mysite\db.sqlite3", check_same_thread=False)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    def _conditional_insert(self, tx, item):
        tx.execute(
            "insert into one_kormovie (title,style,date,place,img) "
            "values(?,?,?,?,?)", (item['title'], item['style'], item[
                'date'], item['place'], item['img'])
        )

    def handle_error(self, e):
        log.err(e)


class OnePipeline(object):

    def __init__(self):
        self.file = codecs.open('items.json', mode='a',  encoding="utf-8")

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode('unicode_escape'))

        return item

    def spider_closed(self, spider):
        self.file.close()


class TwoPipeline(object):

    def __init__(self):
        self.file = codecs.open('items.json', mode='w',  encoding="utf-8")
        pass
