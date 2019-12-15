# -*- coding: utf-8 -*-
import requests
import execjs
from lxml import etree

s = requests.Session()
def get_hidden():
    url='https://ssl.jxufe.edu.cn/cas/login?service=http%3A%2F%2Fecampus.jxufe.edu.cn%2Fc%2Fportal%2Flogin'
    response=s.get(url=url)
    html=etree.HTML(response.text)
    lt=html.xpath('//*[@id="fm1"]/input[@name="lt"]/@value')[0]
    return lt

def login(lt,username):

    # 对密码加密的解决
    with open('E:\learning\webDesignLearning\js\jufeLogin.js', 'r') as f:
        file = f.read()
    ctx = execjs.compile(file)
    password = ctx.call('returnValue')

    #构造formdata
    formdata={
        'username':username,
        'password':password,
        'errors':'0',
        'imageCodeName':"",
        '_rememberMe':'on',
        'cryptoType':"1",
        'lt':lt,
        '_eventId': 'submit'
    }
    #构造headers
    headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'ssl.jxufe.edu.cn',
        'Origin':'https://ssl.jxufe.edu.cn',
        'Referer':'https://ssl.jxufe.edu.cn/cas/login?service=http%3A%2F%2Fecampus.jxufe.edu.cn%2Fc%2Fportal%2Flogin%3Fredirect%3D%252Fc',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

    #开始请求

    index=s.post(url=url,data=formdata,headers=headers,allow_redirects=True)
    test=s.get('http://ecampus.jxufe.edu.cn/web/guest/accountsecurity')
    return test

if __name__=="__main__":
    username = '2201702841'
    lt=get_hidden()
    index=login(lt,username).text
    print(index)




