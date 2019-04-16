# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import urljoin,urlencode
from ArticleSpider.items import ArticleItem
from ArticleSpider.items import Article_loader
import datetime
from scrapy.loader import ItemLoader

class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        #获取文章的url并且传给解析函数
        nodes=response.css('.post.floated-thumb')
        for node in nodes:
            post_url=node.css('.post-meta a.archive-title::attr(href)').extract_first()
            front_image_url=node.css('.post-thumb img::attr(src)').extract_first()
            yield Request(url=response.urljoin(post_url),callback=self.parse_detail,meta={'front_image':front_image_url})

        #提取下一页的Url并且发出请求
        next_url=response.css('.next.page-numbers::attr(href)').extract_first()
        if next_url:
            yield Request(url=next_url,callback=self.parse)

    def parse_detail(self,response):
        # item=ArticleItem()
        # item['title']=response.xpath('//h1/text()').extract_first()
        # try:
        #     date=response.css('.entry-meta-hide-on-mobile::text').extract_first().strip().replace('·',"")
        #     date=datetime.datetime.strptime(date,"%Y/%m/%d").date()
        # except:
        #     date=datetime.datetime.now()
        # item['date']=date
        # item['front_image_url']=response.meta.get('front_image',"") #封面图
        #使用ItemLoader保存Item
        item_loader=Article_loader(item=ArticleItem(),response=response)
        item_loader.add_xpath('title','//h1/text()')
        item_loader.add_css('date','.entry-meta-hide-on-mobile::text')
        item_loader.add_value('front_image_url',response.meta.get('front_image',""))
        item=item_loader.load_item()
        yield item