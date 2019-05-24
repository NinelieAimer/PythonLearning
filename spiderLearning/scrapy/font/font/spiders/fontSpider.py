# -*- coding: utf-8 -*-
import scrapy
from font.settings import FONT_TYPE
from scrapy import Request
from font.items import FontItem

class FontspiderSpider(scrapy.Spider):
    name = "fontSpider"


    def start_requests(self):
        start_url='http://www.17ziti.com/'
        yield Request(url=start_url,callback=self.parse)

    def parse(self,response):
        #获取下一个url判断字体，然后进入，首先获取字符串

        tem_url=response.css('div.nav').xpath('.//li[{}]/a/@href'.format(FONT_TYPE)).extract_first()
        type_url=response.urljoin(tem_url)
        yield Request(url=type_url,callback=self.tff_html)

    #每个字体爬取规则定义
    def tff_html(self,response):
        test=response.body
        #找到每个url具体页面，然后发送request
        url_list=response.css('div.divleft2 dl dd')

        #遍历然后提取单个链接
        for unit in url_list:
            url=response.urljoin(unit.xpath('./a/@href').extract_first())
            name=unit.xpath('./a/@title').extract_first()
            yield Request(url=url,meta={'name':name},callback=self.parse_detail)

        #进行翻页，反复解析
        next_page=response.urljoin(response.css('div.divleft2 ul li:nth-last-child(3) a::attr(href)').extract_first())
        yield Request(url=next_page,callback=self.tff_html)


    def parse_detail(self,response):
        item = FontItem()
        download_url=response.xpath('//ul[@class="downlist"]/li[1]/a/@href').extract_first()
        check=download_url[0:11]
        if download_url[0:11]=='http://down':
            item['name']=response.meta['name']
            item['file_url']=download_url
            yield item



