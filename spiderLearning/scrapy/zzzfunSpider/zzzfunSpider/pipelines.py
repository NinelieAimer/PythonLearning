# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

class ZzzfunspiderPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        url=item['url']
        season=item['season']
        yield Request(url=url,meta={'name':item['name'],
                                    'season':season})

    def file_path(self, request, response=None, info=None):
        return '{}/{}.mp4'.format(request.meta['season'],request.meta['name'])