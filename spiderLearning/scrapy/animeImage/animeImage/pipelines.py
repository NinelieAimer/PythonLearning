# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline

class ImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        url = item['img_url']
        yield Request(url=url)

    def item_completed(self, results, item, info):
        image_paths=[x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem('failed')
        return item

class FilePipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        url = item['img_url']
        yield Request(url=url)

    def item_completed(self, results, item, info):
        image_paths=[x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem('failed')
        return item
