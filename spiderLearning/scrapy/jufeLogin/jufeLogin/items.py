# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ParseItem(scrapy.Item):
    name=scrapy.Field()
    teacher=scrapy.Field()
    MyName=scrapy.Field()