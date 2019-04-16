# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import codecs
import json
from scrapy.exporters import CsvItemExporter
import MySQLdb

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

class ArtileImagePipline(ImagesPipeline):
    def item_completed(self, results, item, info):
        image_paths=[X['path'] for ok,X in results if ok]
        item['front_image_path']=image_paths
        if not image_paths:
            raise DropItem('failed')
        return item
    def get_media_requests(self, item, info):
        yield Request(url=item['front_image_url'])

class JsonPipeline(object):
    def __init__(self):
        self.file=codecs.open('article.json','w',encoding='utf-8')
    def process_item(self,item,spider):
        lines=json.dumps(dict(item),ensure_ascii=False)+'\n'   #dumps是将字典转化为json格式的一个东西，还有一个ensure_ascii非常重要
        self.file.write(lines)
        return item
    def spider_closed(self,spider):
        self.file.close()

class testPipeline(object):
    def __init__(self):
        self.file = open('test.csv', 'wb')
    def open_spider(self,spider):
        self.exporter=CsvItemExporter(file=self.file,encoding='utf-8')
        self.exporter.start_exporting()
    def process_item(self,item,spider):
        self.exporter.fields_to_export=['title','date']
        self.exporter.export_item(item)
        return item
    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()

class MysqlPipeline(object):
    def __init__(self):
        self.host='127.0.0.1'
        self.user='root'
        self.password='asd369258'
        self.db='article'

    def open_spider(self,spider):
        self.con=MySQLdb.connect(host=self.host,user=self.user,password=self.password,database=self.db,charset='utf8',use_unicode=True)
        self.cursor=self.con.cursor()

    def process_item(self,item,spider):
        sql='''
            insert into article(title,date,front_image_url)
            values(%s,%s,%s)
        '''
        self.cursor.execute(sql,(item['title'],item['date'],item['front_image_url']))
        self.con.commit()
