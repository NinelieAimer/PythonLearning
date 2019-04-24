# -*- coding: utf-8 -*-
from scrapy.loader.processors import MapCompose   #这里是import一个处理函数
from scrapy.loader import ItemLoader				#这个是导入一个ItemLoader类，很重要，后面要继承
from scrapy.loader.processors import TakeFirst
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PracticeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class profitItem(scrapy.Item):
    #提取利润表
    STOCK_NUMBER=scrapy.Field()
    YEAREND_DATE_PROFIT=scrapy.Field()
    TURNOVER=scrapy.Field()
    PBT=scrapy.Field()
    OPER_PROFIT=scrapy.Field()
    NET_PROF=scrapy.Field()
    INCOME_NETTRADING=scrapy.Field()
    INCOME_NETFEE=scrapy.Field()
    INCOME_INTEREST=scrapy.Field()
    EPS=scrapy.Field()
    DPS=scrapy.Field()

class assetsItem(scrapy.Item):
    STOCK_NUMBER=scrapy.Field()
    YEAREND_DATE_ASSETS=scrapy.Field()
    TOTAL_LIAB=scrapy.Field()
    TOTAL_DEBT=scrapy.Field()
    TOTAL_ASS=scrapy.Field()
    OTHER_ASS=scrapy.Field()
    LOAN_TO_BANK=scrapy.Field()
    INVENTORY=scrapy.Field()
    FIX_ASS=scrapy.Field()
    FINANCIALASSET_SALE=scrapy.Field()
    EQUITY=scrapy.Field()
    DERIVATIVES_LIABILITIES=scrapy.Field()
    DERIVATIVES_ASSET=scrapy.Field()
    DEPOSITS_FROM_CUSTOMER=scrapy.Field()
    CURR_LIAB=scrapy.Field()
    CURR_ASS=scrapy.Field()
    CASH_SHORTTERMFUND=scrapy.Field()
    CASH=scrapy.Field()

class cashItem(scrapy.Item):
    STOCK_NUMBER=scrapy.Field()
    YEAREND_DATE_CASH=scrapy.Field()
    CF_NCF_OPERACT=scrapy.Field()
    CF_INV=scrapy.Field()
    CF_INT_REC=scrapy.Field()
    CF_INT_PAID=scrapy.Field()
    CF_FIN_ACT=scrapy.Field()
    CF_EXCH=scrapy.Field()
    CF_END=scrapy.Field()
    CF_DIV_REC=scrapy.Field()
    CF_DIV_PAID=scrapy.Field()
    CF_CHANGE_CSH=scrapy.Field()
    CF_BEG=scrapy.Field()





