# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import urljoin
class JufeloginSpider(scrapy.Spider):
    name = "jufeLogin"

    def start_requests(self):
        url='http://ecampus.jxufe.edu.cn/web/guest/student'
        yield Request(url=url,callback=self.parse,meta={'UseSelenium':True})

    def parse(self, response):
        temp_url=response.css('.personal-info a::attr(href)').extract_first()
        next_url=response.urljoin(temp_url)
        cookies=response.meta['cookies']
        if temp_url[-10:]=='usercenter':
            self.logger.info('successful login')
            yield Request(url=next_url,callback=self.profile,cookies=cookies)
        else:
            self.logger.info('login failed')

    def profile(self,response):
        pass
