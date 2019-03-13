# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from scrapy.http import Request
from animeImage.items import AnimeimageItem
from scrapy import log

class ImagesSpider(scrapy.Spider):
    name = "images"
    allowed_domains = ["anime-pictures.net"]

    def start_requests(self):
        #构造参数设置搜索文件
        data={
            "search_tag":"miku",
            "lang":"en"
        }
        #构造基本的url
        base_url="https://anime-pictures.net/pictures/view_posts/0?"
        param=urlencode(data)
        url=base_url+param
        yield Request(url=url,callback=self.parse)

    def parse(self, response):
        #生成下一页的request
        next=response.xpath('//div[@id="posts"]/div[3]/p/a[last()]/@href').extract_first()
        if next:
            next_url=response.urljoin(next)
            yield Request(url=next_url,callback=self.parse)
        else:
            self.logger.info("no more page")
            return

        #提取图片网址，发送请求
        img_list=response.css("#posts .img_block_big a::attr(href)").extract()
        for url in img_list:
            img_url=response.urljoin(url)
            yield Request(url=img_url,callback=self.download)

    #解析页面生成Item对象
    def download(self,response):
        item=AnimeimageItem()
        img_url=response.css('.download_icon::attr(href)').extract_first()
        item['img_url']=response.urljoin(img_url)
        item['title']=response.css('#cont > div:nth-child(1) > div:nth-child(1) > h1::text').extract_first()
        yield item