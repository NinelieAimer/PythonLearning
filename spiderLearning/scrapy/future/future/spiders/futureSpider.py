# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
from scrapy.http import JSONRequest
from future.items import FutureItem
class FuturespiderSpider(scrapy.Spider):
    name = 'futureSpider'


    def start_requests(self):
        data = {"page": '1', "per_page": '200', "UUID": "", "NickName": "", "School": "", "CompanyName": "", "Type": ""}
        post_url = 'http://edu.czce.com.cn/api/cupSearch'
        yield JSONRequest(url=post_url,data=data)

    def parse(self, response):
        dict=json.loads(response.text)
        for person in dict['cupSearchResults']:
            data={
                'per_page':'10',
                'UUID': person['UUID']
            }
            yield JSONRequest(url='http://edu.czce.com.cn/api/cupPersonalResult',data=data,callback=self.gen_item,
                              meta={
                                  'company':person['CompanyName'],
                                  'school':person['School'],
                                  'rank':person['Ranks'],
                                  'mobile':person['Mobile']
                              })

    def gen_item(self,response):
        dict=json.loads(response.text)
        item=FutureItem()
        item['company']=response.meta['company']
        item['school']=response.meta['school']
        item['rank']=response.meta['rank']
        item['personal']=json.loads(response.text)['cupResults']
        item['mobile']=response.meta['mobile']
        yield item
