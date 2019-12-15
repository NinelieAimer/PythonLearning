#引入和准备工作
from lxml import etree
import  requests

url="https://www.baidu.com"
response=requests.get(url)
result=etree.HTML(response.text)    #注意这里要传入文本对象

lis=result.xpath("//div//a")
print(lis)
parent=result.xpath("//*[@id='su']/..")
print(parent)
time=result.xpath('//*[@id="s_top_wrap"]/div[1]')
print(time)

#getattribute
getattrbute=result.xpath('//*[@id="kw"]/@class')
print(getattrbute)

#contains
contain=result.xpath('//span[contains(@class,"btn_wr") and @id="s_btn_wr"]')
print(contain)