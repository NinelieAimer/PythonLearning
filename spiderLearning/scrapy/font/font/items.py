# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FontItem(scrapy.Item):
    name=scrapy.Field()
    file_url=scrapy.Field()
