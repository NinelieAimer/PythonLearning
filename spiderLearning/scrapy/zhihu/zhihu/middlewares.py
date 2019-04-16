# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from fake_useragent import UserAgent
import time
from scrapy.http import HtmlResponse


class ZhihuSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class zhihuLoginMiddleware(object):

    def __init__(self,ZHIHU_USERNAME,ZHIHU_PASSWORD,JUFE_USERNAME,JUFE_PASSWORD):
        self.zhihu_username=ZHIHU_USERNAME
        self.zhihu_password=ZHIHU_PASSWORD
        self.jufe_username=JUFE_USERNAME
        self.jufe_password=JUFE_PASSWORD

    @classmethod
    def from_crawler(cls,crawler):
        ZHIHU_USERNAME=crawler.settings.get('ZHIHU_USERNAME')
        ZHIZHU_PASSWORD=crawler.settings.get('ZHIHU_PASSWORD')
        JUFE_USERNAME=crawler.settings.get('JUFE_USERNAME')
        JUFE_PASSWORD=crawler.settings.get('JUFE_PASSWORD')
        return cls(ZHIHU_USERNAME,ZHIZHU_PASSWORD,JUFE_USERNAME,JUFE_PASSWORD)

    def process_request(self,request,spider):
        if request.url=='https://www.zhihu.com/signin?next=%2F':
            browser=webdriver.Chrome()
            browser.get(request.url)
            browser.find_element_by_xpath('//input[@name="username"]').send_keys(self.zhihu_username)
            browser.find_element_by_xpath('//input[@name="password"]').send_keys(self.zhihu_password)
            time.sleep(5)
            browser.find_element_by_xpath('//button[@type="submit"]').click()
            time.sleep(1)
            source=browser.page_source
            return HtmlResponse(body=source,encoding='utf-8')

class JufeLoginMiddleware(object):
    def __init__(self,JUFE_USERNAME,JUFE_PASSWORD):
        self.username=JUFE_USERNAME
        self.password=JUFE_PASSWORD
        self.browser=webdriver.Chrome()

    @classmethod
    def from_crawler(cls, crawler):
        JUFE_USERNAME = crawler.settings.get('JUFE_USERNAME')
        JUFE_PASSWORD = crawler.settings.get('JUFE_PASSWORD')
        return cls(JUFE_USERNAME, JUFE_PASSWORD)

    def process_request(self,request,spider):
        if request.meta.get('UseSelenium'):   #判断是否需要使用selenium
            #使用selenium登入
            self.browser.get(url='https://ssl.jxufe.edu.cn/cas/login')
            self.browser.find_element_by_id('username').send_keys(self.username)
            self.browser.find_element_by_id('password').send_keys(self.password)
            self.browser.find_element_by_xpath('//input[@type="submit"]').click()
            time.sleep(3)

            #防止重复爬取，直接可以
            request.meta['UseSelenium']=False
            selenium_cookies=self.browser.get_cookies()
            request.meta['cookies']=selenium_cookies
            return HtmlResponse(url=request.url,body=self.browser.page_source,encoding='utf-8')
        else:
            #进行user-agent
            ua=UserAgent()
            request.headers['user-agent']=ua.chrome

