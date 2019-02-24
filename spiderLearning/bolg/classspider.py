import requests
from lxml import etree
import re

class BoleSpider():

    def get_text(self,start_url):
        html=requests.get(url=start_url,timeout=3)
        return html.text

    def get_list(self,html_text):
        html=etree.HTML(html_text)
        response=html.xpath('//a[@class="archive-title"]/@href')
        return response

    def changepage(self,html_text):
        html = etree.HTML(html_text)
        response=html.xpath('//a[@class="next page-numbers"]/@href')
        return  response

    def parse(self,url):
        info={}
        html=self.get_text(start_url=url)
        html=etree.HTML(html)

        info['title']=html.xpath('//div[@class="entry-header"]/h1/text()')[0]   #获取标题

        info['time']=html.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()')[0].strip().replace(' ·','')   #获取时间

        favor=html.xpath('//span[contains(@class,"bookmark-btn")]/text()')  #获取收藏
        match=re.match(r'.*?(\d+).*',favor[0])
        if match:
            info["favorite"]=match.group(1)
        else:
            info["favorite"]=""

        return info

    def writeinfo(self,info):
        f=open('info.txt','a+')
        f.writelines("文章标题为:{}\n".format(info['title']))
        f.writelines("文章的时间为:{}\n".format(info['time']))
        f.writelines("文章的收藏量为:{}\n".format(info['favorite']))
        f.writelines("\n")
        f.close()

