# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
import datetime

class Article_loader(ItemLoader):
    default_output_processor = TakeFirst()

class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def add_some(value):
    return value+'successful'

def date_process(value):
    date=value.strip().replace('·',"")
    try:
        date = datetime.datetime.strptime(date, "%Y/%m/%d").date()
    except:
        date = datetime.datetime.now()
    return date

class ArticleItem(scrapy.Item):
    title=scrapy.Field(
        input_processor=MapCompose(add_some)
    )
    date=scrapy.Field(
        input_processor=MapCompose(date_process)
    )
    front_image_url=scrapy.Field()
    front_image_path=scrapy.Field()
