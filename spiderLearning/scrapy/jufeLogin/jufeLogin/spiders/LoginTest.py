# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy import Request
from jufeLogin.items import ParseItem

class LogintestSpider(scrapy.Spider):
    name = "LoginTest"

    def start_requests(self):
        url='https://ssl.jxufe.edu.cn/cas/login'
        yield Request(url=url,callback=self.parse)

    def parse(self, response):
        It=response.xpath('//*[@id="fm1"]/input[2]/@value').extract_first()
        formdata={
            'username':'2201702841',
            'password':'jkl147258',
            'It':It
        }
        return FormRequest.from_response(response,formdata==formdata,callback=self.after_login)

    def after_login(self,response):
        self.logger.info("successful")
        item=ParseItem()
        item['name']=response.url
        item['teacher']=response.xpath('//*[@id="layout_2"]/a/span/text()').extract_first()
        yield item