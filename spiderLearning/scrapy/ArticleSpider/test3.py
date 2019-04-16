# -*- coding: utf-8 -*-
import requests
import execjs
from lxml import etree
from urllib.parse import urljoin

#先把s实例化
# s=requests.Session()
#
# #找到lt，并返回
# def get_post_url():
#     base_url='https://ssl.jxufe.edu.cn/cas/login?service=http%3A%2F%2Fecampus.jxufe.edu.cn%2Fc%2Fportal%2Flogin'
#     response = s.get(url=base_url)
#     html = etree.HTML(response.text)
#     test = html.xpath('//form[@id="fm1"]/@action')[0]
#     post_url = urljoin(base_url, test)
#     return post_url

def login():
    #获取post_url,lt参数
    s=requests.session()
    base_url = 'https://ssl.jxufe.edu.cn/cas/login?service=http%3A%2F%2Fecampus.jxufe.edu.cn%2Fc%2Fportal%2Flogin'

    response = s.get(url=base_url)
    html = etree.HTML(response.text)
    test = html.xpath('//form[@id="fm1"]/@action')[0]

    #获取post的Url
    post_url = urljoin(base_url, test)

    #获取lt
    lt = html.xpath('//*[@id="fm1"]/input[@name="lt"]/@value')[0]


    # 对密码加密的解决
    with open('E:\learning\webDesignLearning\js\jufeLogin.js', 'r') as f:
        file = f.read()
    ctx = execjs.compile(file)
    password = ctx.call('returnValue')

    # 构造formdata
    formdata = {
        'username': '2201702841',
        'password': '16934a0657533c276510323289ceab8d3fc248cf4e5c5fc2049a807ab75857b15f8572e9cbffd419a56500baf39bbcb9f590033c4ebc1eee1b727bf3e8be9127e468c45e18d8435325bd697adf268a3c9a6cacda6058a5637e8419febb46f3e0621dbde4f42e52f0f87a6fa4851f915c0896393aba6945dbff8d6ede8a1e748b',
        'errors':'0',
        'imageCodeName': "",
        '_rememberMe': 'on',
        'cryptoType': "1",
        'lt': lt,
        '_eventId': 'submit'
    }
    # 构造headers
    headers = {
        'Host': 'ssl.jxufe.edu.cn',
        'Origin': 'https://ssl.jxufe.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\
                   51.0.2704.84 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Referer': "https://ssl.jxufe.edu.cn/cas/login?service=http%3A%2F%2Fecampus.jxufe.edu.cn%2Fc%2Fportal%2Flogin"
    }


    index=s.post(url=post_url,data=formdata)
    item=s.get(url='http://ecampus.jxufe.edu.cn/web/guest/accountsecurity')
    print(item.text)

    return index

if __name__=="__main__":
    a=login()

