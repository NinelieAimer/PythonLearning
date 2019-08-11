# -*- coding: utf-8 -*-
import scrapy
from zzzfunSpider.settings import  NAME
from scrapy import Request
from scrapy_selenium import SeleniumRequest
from zzzfunSpider.items import ZzzfunspiderItem

class ZzzfunSpider(scrapy.Spider):
    name = 'zzzfun'

    def start_requests(self):
        url='http://www.zzzfun.com/vod-search.html?wd='+NAME
        yield Request(url=url,callback=self.parse)

    def parse(self, response):

        #获取搜索到的列表
        list_url=response.css('.show-list li').xpath('./a/@href').extract()
        list_names=response.css('.show-list li').xpath('./div/h2/a/text()').extract()
        list=dict(zip(list_names,list_url))

        #选择想要下载的动漫，获得列表
        choose=input('选择你想下载的动漫{}，用\"-\"隔开'.format(list_names)).split(sep='-')
        for season in choose:
            url=list[season]
            yield Request(url=response.urljoin(url),callback=self.find_url,meta={'season':season})

    def find_url(self,response):
        url_list=response.css('.episode-wrap').xpath('./ul[1]//li/a/@href').extract()
        episodes=response.css('.episode-wrap').xpath('./ul[1]//li//span/text()').extract()
        find_lists=dict(zip(episodes,url_list))
        self.logger.info('你将下载{}'.format(find_lists.keys()))
        for key in find_lists:
            url=response.urljoin(find_lists[key])
            yield SeleniumRequest(url=url,callback=self.get_php,dont_filter=True,wait_time=200,encoding='utf-8',meta={'name':key,
                                                                                                                      'season':response.meta['season']})

    def get_php(self,response):
        self.logger.info(response.request.meta['driver'].title)
        php_url=response.xpath("//*[@id='playleft']/iframe/@src").extract_first()
        real_url=response.urljoin(php_url)
        yield Request(url=real_url,callback=self.get_download,meta={'name':response.meta['name'],
                                                                    'season':response.meta['season']})

    def get_download(self,response):
        item=ZzzfunspiderItem()
        item['url']=response.xpath('//*[@id="video"]/source/@src').extract_first()
        item['name']=response.meta['name']
        item['season']=response.meta['season']
        yield item
