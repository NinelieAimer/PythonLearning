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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def __init__(self,ZHIHU_USERNAME,ZHIHU_PASSWORD):
        #获取知乎的账号密码
        self.zhihu_username=ZHIHU_USERNAME
        self.zhihu_password=ZHIHU_PASSWORD

        #进行不加载图片
        chrome_options=webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.browser=webdriver.Chrome()

    @classmethod
    def from_crawler(cls,crawler):
        ZHIHU_USERNAME=crawler.settings.get('ZHIHU_USERNAME')
        ZHIZHU_PASSWORD=crawler.settings.get('ZHIHU_PASSWORD')
        return cls(ZHIHU_USERNAME,ZHIZHU_PASSWORD)

    def process_request(self,request,spider):
        if request.meta['UseSelenium']:
            self.browser.get('https://www.zhihu.com/signin?next=%2F')
            self.browser.find_element_by_xpath('//input[@name="username"]').send_keys(self.zhihu_username)
            self.browser.find_element_by_xpath('//input[@name="password"]').send_keys(self.zhihu_password)
            time.sleep(5)
            button=self.browser.find_element_by_xpath('//button[@type="submit"]')
            time.sleep(3)

            #把flag改为false,并保存cookie作为meta传递出去
            request.meta['UseSelenium']=False
            request.meta['cookies']=self.browser.get_cookies()

            #传递response
            return HtmlResponse(body=self.browser.page_source,encoding='utf-8',url=request.url)

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

