# -*- coding: utf-8 -*-
from scrapy.exporters import CsvItemExporter
from practice.items import cashItem,assetsItem,profitItem
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class profitItemPipline(object):
    def __init__(self):
        self.file_profit=open(file='profit.csv',mode='wb')
        self.file_assets=open('asset.csv', 'wb')
        self.file_cash = open('cash.csv', 'wb')

    def open_spider(self,spider):
        self.exporter_profit=CsvItemExporter(file=self.file_profit,encoding='utf-8')
        self.exporter_assets= CsvItemExporter(file=self.file_assets,encoding='utf-8')
        self.exporter_cash = CsvItemExporter(file=self.file_cash, encoding='utf-8')
        self.exporter_profit.start_exporting()
        self.exporter_assets.start_exporting()
        self.exporter_cash.start_exporting()



    def process_item(self,item,spider):
        if isinstance(item,profitItem):
            self.exporter_profit.fields_to_export=['STOCK_NUMBER','YEAREND_DATE_PROFIT','TURNOVER','PBT','OPER_PROFIT','NET_PROF','INCOME_NETTRADING','INCOME_NETFEE','INCOME_INTEREST','EPS','DPS']
            self.exporter_profit.export_item(item)
            return item
        elif isinstance(item,assetsItem):
            self.exporter_assets.fields_to_export = ['STOCK_NUMBER','YEAREND_DATE_ASSETS', 'TOTAL_LIAB', 'TOTAL_DEBT', 'TOTAL_ASS',
                                              'OTHER_ASS', 'LOAN_TO_BANK', 'INVENTORY', 'FIX_ASS',
                                              'FINANCIALASSET_SALE', 'EQUITY', 'DERIVATIVES_LIABILITIES',
                                              'DERIVATIVES_ASSET', 'DEPOSITS_FROM_CUSTOMER', 'CURR_LIAB', 'CURR_ASS',
                                              'CASH_SHORTTERMFUND', 'CASH']
            self.exporter_assets.export_item(item)
            return item
        else:
            self.exporter_cash.fields_to_export=[
                'STOCK_NUMBER','YEAREND_DATE_CASH','CF_NCF_OPERACT','CF_INV','CF_INT_REC','CF_INT_PAID','CF_FIN_ACT','CF_EXCH',
                'CF_END','CF_DIV_REC','CF_DIV_PAID','CF_CHANGE_CSH','CF_BEG'
            ]
            self.exporter_cash.export_item(item)
            return item


    def close_spider(self,spider):
        self.exporter_profit.finish_exporting()
        self.exporter_assets.finish_exporting()
        self.exporter_cash.finish_exporting()
        self.file_profit.close()
        self.file_assets.close()
        self.file_cash.close()


