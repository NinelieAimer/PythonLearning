# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import urlencode
from taobao.items import TaobaoItem

class TaobaospiderSpider(scrapy.Spider):
    name = "taobaoSpider"
    allowed_domains = ["taobao.com"]


    def start_requests(self):


        data={
            'q':"miku手办",
            "s":"22"
        }
        param=urlencode(data)
        base_url="https://s.taobao.com/search?"
        url=base_url+param
        yield Request(url=url,callback=self.parse)

    def parse(self, response):
        item=TaobaoItem()
        list=response.css(".ctx-box.J_MouseEneterLeave.J_IconMoreNew")
        for div in list:
            item['id']=div.xpath('.//div[contains(@class,"row-2")]/a/@href').extract_first()
            item['name']=div.xpath('.//div[contains(@class,"row-3")]//a/span[2]/text()').extract_first()
            item['price']=div.xpath('.//div[contains(@class,"row-1")]//div[@class="price"]/strong/text()').extract_first()
            self.logger.info(item['price'])
            yield item