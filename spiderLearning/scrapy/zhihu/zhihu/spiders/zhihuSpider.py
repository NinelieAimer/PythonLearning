# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class ZhihuspiderSpider(scrapy.Spider):
    name = "zhihuSpider"
    allowed_domains = ["zhihu.com"]


    def start_requests(self):
        login_url='https://www.zhihu.com/signin?next=%2F'
        yield Request(url=login_url,callback=self.parse)

    def parse(self, response):
        pass