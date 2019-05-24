# -*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FontPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        url=item['file_url']
        yield Request(url=url)

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem('failed')
        return item




