# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy import Request
from jufeLogin.items import ParseItem
import json

class LogintestSpider(scrapy.Spider):
    name = "LoginTest"

    def start_requests(self):
        url='https://ssl.jxufe.edu.cn/cas/login?service=http%3A%2F%2Fecampus.jxufe.edu.cn%2Fc%2Fportal%2Flogin'
        yield Request(url=url,callback=self.parse)

    def parse(self, response):
        It=response.xpath('//*[@id="fm1"]/input[2]/@value').extract_first()
        self.logger.info(It)
        formdata={
            'username':'2201702841',
            'password':'jkl147258',
            'errors':'0',
            'imageCodeName':'',
            '_rememberMe':'on',
            'cryptoType':'1',
            'It':It,
            '_eventId':'submit'
        }
        return FormRequest.from_response(response,formdata=formdata,callback=self.student_path,dont_filter=True)


    def student_path(self,response):

        #开始发送请求,测试是否成功
        headers={
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Referer":'http://ecampus.jxufe.edu.cn/web/guest/student',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
        }

        url_test='http://ecampus.jxufe.edu.cn/web/guest/student?p_p_id=indexmessage_WAR_jigsawportalindexmessageportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=load&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_count=2&t=1553348519889'
        yield Request(url=url_test,headers=headers,callback=self.get_name_test,dont_filter=True)

        #准备爬取的url
        yield Request(url='http://xfz.jxufe.edu.cn/portal/main.xsp/page/-1/?.a.p=aT0lMkZ4Znpwb3J0YWwlMkZzZWxlY3RTdWJqZWN0UmVzdWx0NFN0dWRlbnQmdD1yJnM9bm9ybWFs%0AJmVzPWRldGFjaCZtPXZpZXc%3D&mlinkf=showSchedule.jsp',dont_filter=True,callback=self.go_student)



    def get_name_test(self,response):
        self.logger.info("===============successful==================")
        list=json.loads(response.text)
        self.logger.info(list.get("data")["userName"]+"登入成功")

    def go_student(self,response):
        self.logger.info(response.text)
