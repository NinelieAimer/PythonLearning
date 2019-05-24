# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
from pyquery import PyQuery as pq

ua=UserAgent()
# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html


class RandomHeader(object):
    def process_requests(self,request,spider):
        #换头
        request.headers['User-Agent']=ua.chrome

        #换IP
        html = pq(url="http://p.ashtwo.cn/")
        ip = html('p').text()
        request.meta['proxy']='http://'+ip