# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from FreeProxy.items import FreeproxyItem

class IpproxySpider(scrapy.Spider):
    name = "IpProxy"
    allowed_domains = ["kuaidaili.com"]

    def start_requests(self):
        for i in range(1,2769):
            url='https://www.kuaidaili.com/free/inha/{}/'.format(i)
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        #提取Ip
        item=FreeproxyItem()
        list=response.xpath('//body//tbody//tr')
        for tr in list:
            item['Ip']=tr.xpath('./td[1]/text()').extract_first()
            item["Port"]=tr.xpath('./td[2]/text()').extract_first()
            yield item