# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from practice.settings import STOCK_NUMBER
import json
from practice.items import profitItem,cashItem,assetsItem

class StockSpider(scrapy.Spider):
    name = "stock"
    allowed_domains = ["http://quotes.money.163.com"]


    def start_requests(self):
        start_url='http://quotes.money.163.com/hkstock/cwsj_'+STOCK_NUMBER+'.html'
        yield Request(url=start_url,callback=self.parse)


    def parse(self, response):
        #获取利润表的开始时间和结束时间
        profit_start_time=response.css('#lrb1').xpath('.//option[last()]/text()').extract_first()
        profit_end_time=response.css('#lrb2').xpath('.//option[1]/text()').extract_first()

        #获取资产负债表的开始和结束时间
        assets_start_time=response.css('#fzb1').xpath('.//option[last()]/text()').extract_first()
        assets_end_time=response.css('#fzb2').xpath('.//option[1]/text()').extract_first()

        #获取现金流量表
        cash_start_time=response.css('#llb1').xpath('.//option[last()]/text()').extract_first()
        cash_end_time=response.css('#llb2').xpath('.//option[1]/text()').extract_first()

        profit_url='http://quotes.money.163.com/hk/service/cwsj_service.php?symbol='+STOCK_NUMBER+'&start={}&end={}&type=lrb&unit=yuan'.format(profit_start_time,profit_end_time)
        assets_url='http://quotes.money.163.com/hk/service/cwsj_service.php?symbol='+STOCK_NUMBER+'&start={}&end={}&type=fzb&unit=yuan'.format(assets_start_time,assets_end_time)
        cash_url='http://quotes.money.163.com/hk/service/cwsj_service.php?symbol='+STOCK_NUMBER+'&start={}&end={}&type=llb&unit=yuan'.format(cash_start_time,cash_end_time)

        yield Request(url=profit_url,callback=self.profit,dont_filter=True)
        yield Request(url=assets_url,callback=self.assets,dont_filter=True)
        yield Request(url=cash_url,callback=self.cash,dont_filter=True)

    def profit(self,response):
        #实例化item
        profit_item=profitItem()

        #读取每个列表中的json数据
        list=json.loads(response.text)
        for item in list:
            profit_item['STOCK_NUMBER']=STOCK_NUMBER
            profit_item['YEAREND_DATE_PROFIT']=item['YEAREND_DATE']
            profit_item['TURNOVER']=item['TURNOVER']
            profit_item['PBT']=item['PBT']
            profit_item['OPER_PROFIT']=item['OPER_PROFIT']
            profit_item['NET_PROF']=item['NET_PROF']
            profit_item['INCOME_NETTRADING']=item['INCOME_NETTRADING']
            profit_item['INCOME_NETFEE']=item['INCOME_NETFEE']
            profit_item['INCOME_INTEREST']=item['INCOME_INTEREST']
            profit_item['EPS']=item['EPS']
            profit_item['DPS']=item['DPS']

            yield profit_item

    def assets(self,response):
        assets_item=assetsItem()

        list=json.loads(response.text)
        for item in list:
            assets_item['STOCK_NUMBER']=STOCK_NUMBER
            assets_item['YEAREND_DATE_ASSETS']=item['YEAREND_DATE']
            assets_item['TOTAL_LIAB']=item['TOTAL_LIAB']
            assets_item['TOTAL_DEBT']=item['TOTAL_DEBT']
            assets_item['TOTAL_ASS']=item['TOTAL_ASS']
            assets_item['OTHER_ASS']=item['OTHER_ASS']
            assets_item['LOAN_TO_BANK']=item['LOAN_TO_BANK']
            assets_item['INVENTORY']=item['INVENTORY']
            assets_item['FIX_ASS']=item['FIX_ASS']
            assets_item['FINANCIALASSET_SALE']=item['FINANCIALASSET_SALE']
            assets_item['EQUITY']=item['EQUITY']
            assets_item['DERIVATIVES_LIABILITIES']=item['DERIVATIVES_LIABILITIES']
            assets_item['DERIVATIVES_ASSET']=item['DERIVATIVES_ASSET']
            assets_item['DEPOSITS_FROM_CUSTOMER']=item['DEPOSITS_FROM_CUSTOMER']
            assets_item['CURR_LIAB']=item['CURR_LIAB']
            assets_item['CURR_ASS']=item['CURR_ASS']
            assets_item['CASH_SHORTTERMFUND']=item['CASH_SHORTTERMFUND']
            assets_item['CASH']=item['CASH']

            yield assets_item

    def cash(self,response):
        cash_item=cashItem()

        list=json.loads(response.text)
        for item in  list:
            cash_item['STOCK_NUMBER']=STOCK_NUMBER
            cash_item['YEAREND_DATE_CASH']=item['YEAREND_DATE']
            cash_item['CF_NCF_OPERACT']=item['CF_NCF_OPERACT']
            cash_item['CF_INV']=item['CF_INV']
            cash_item['CF_INT_REC']=item['CF_INT_REC']
            cash_item['CF_INT_PAID']=item['CF_INT_PAID']
            cash_item['CF_FIN_ACT']=item['CF_FIN_ACT']
            cash_item['CF_EXCH']=item['CF_EXCH']
            cash_item['CF_END']=item['CF_END']
            cash_item['CF_DIV_REC']=item['CF_DIV_REC']
            cash_item['CF_DIV_PAID']=item['CF_DIV_PAID']
            cash_item['CF_CHANGE_CSH']=item['CF_CHANGE_CSH']
            cash_item['CF_BEG']=item['CF_BEG']

            yield cash_item