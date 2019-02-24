from  classspider import BoleSpider

spider = BoleSpider()
url = "http://blog.jobbole.com/all-posts/"
def main():
    global url  #声明全局
    global spider   #声明全局

    url_list=list() #定义一个空列表
    for i in range(20): #获取所有文章列表
        html=spider.get_text(start_url=url)     #解析页面

        urls=spider.get_list(html_text=html)    #获取页面的所有文章列表
        url_list=urls+url_list                  #加和
        url=spider.changepage(html_text=html)[0]  #获取下一页url

    for one_url in url_list:
        try:
            info=spider.parse(url=one_url)
            spider.writeinfo(info=info)
        except:
            print("{}爬取异常".format(one_url))
main()