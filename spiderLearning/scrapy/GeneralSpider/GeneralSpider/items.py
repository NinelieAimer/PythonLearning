# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field,Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst,Join,Compose

class GeneralspiderItem(scrapy.Item):
    title=Field()
    url=Field()
    text=Field()
    datetime=Field()
    source=Field()
    website=Field()

class NewLoader(ItemLoader):
    default_output_processor = TakeFirst()

class ChinaLoader(NewLoader):
    text_out=Compose(Join(),lambda s:s.strip())
    source_out=Compose(Join(),lambda s:s.strip())
