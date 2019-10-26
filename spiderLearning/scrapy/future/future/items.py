# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FutureItem(scrapy.Item):
    personal=scrapy.Field()
    company=scrapy.Field()
    rank=scrapy.Field()
    school=scrapy.Field()
    mobile=scrapy.Field()
