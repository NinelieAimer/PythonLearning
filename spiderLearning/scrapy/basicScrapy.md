#  Scrapy介绍

## 项目模块：

Engine：引擎是处理核心，类似于内核东西

Item:这是定义爬取结果的数据结构，爬取数据就会变成Item对象

Scheduler:这个是调度器，接受引擎发过来的请求并将其加入队列中，

Downloader:下载器，这个是用来下载内容的，下完给spider

Item pipeline:这个是负责数据清洗、验证和储存数据

## 项目结构

scrapy.cfg:这个是scrapy的配置文件，这里定义了配置文件的路径、部署相关信息

items.py:这里定义Item数据结构，Item的定义都放在这

pipeline.py:定义pipeline实现

setting.py:这个是项目的全局配置

middlewares.py:定义Spider Middlewares和Downloader Middlewares实现

spiders:包含一个个spider的实现，每个Spider都有一个文件夹



# 入门

## 启动项目

从conda中，找到文件夹，输入

```python
scrapy startproject [project name]
```

## 创建spider

进入项目文件夹，输入

```
scrapy genspider [spidername] [域名（不用加www和http）]
```

## 使用选择器

### Scrapy shell

Scrapy shell类似于调试用的东西使用很简单

```
scrapy shell [网址（不用打引号）]
```

### Xpath选择器

首先明确，利用这个选择器是返回一个**SelectorList类型**，SelectorList和Selector都可以继续使用xpath()和css()等方法

示例：

```python   
result=response.xpath('//a')  #这里就返回一个SelectorList类型

result=result.xpath('./img')  #**这里就要注意了，这个.不是指css选择器，而是从这个节点开始选择，不然就会从根目录开始选择的**

result[0] #这里我们就提取一个selector类型，没啥用

result.extract()  #利用extract()方法我们可以得到节点的内容,这里内容是一个节点元素，要提取文本必须要用/text(),/@href这里和xpath一样

result=response.xpath('//a/text()').extract()

#这里就会生成一个文本列表，如果只想第一个就extract_first()
result=response.xpath('//a/text()').extract_first()
```

### CSS选择器

这个和我们Lxml里面那个是差不多的，不过也是返回selectorList类型，注意用extract()

还有注意的是**提取属性方法不同**

```
result=response.css('a::href').extract_fitst() #这里用了::引出属性
```

**css选择器和xpath选择器在这里是可以混用的**



### 正则匹配

re()方法可以**对xpath和css处理过的对象**进行匹配，而且直接会返回一个文本列表，非常方便，还可以用re_first()方法，只获取第一个

```python
response.xpath("//a/text()").re((.*?)test)  #注意这里会直接返回列表，而且只会返回括号里面匹配到的值
```

# spider的用法

# Downloader Middleware用法

**这个方法非常重要，是用来处理到达Downloader的Request和从Downloader出去到达spider的reponse**

使用方法步骤：
定义一个类，类名最后面最后是Middlerware这样好辨认

然后def process_request()或者process_response（）方法，接着在middlerware.py中把，

DOWNLOADER_MIDEDLEWARES={

​		'[项目名称].middlerwares.[类名]'

}

弄出来

# Item Exporters的一些用法

## CsvItemExporter

```python
#因为scrapy的一些问题，csv文件可能会有空行，要选区CsvItemExporter里面进行设置
 self.stream = io.TextIOWrapper(
            file,
            newline="",	#添加这个newline=""，导出的csv中就没有空行了
            line_buffering=False,
            write_through=True,
            encoding=self.encoding
        )

    
    
#在pipeline中的操作
from scrapy.exporters import CsvItemExporter
class testPipeline(object):
    def __init__(self):
        self.file = open('test.csv', 'wb')
        #初始阶段，打开文件，记住一定要用wb
    def open_spider(self,spider):
        self.exporter=CsvItemExporter(file=self.file,encoding='utf-8')  #实例化exporter
        self.exporter.start_exporting()   #开始exporter

    def process_item(self,item,spider):
        self.exporter.fields_to_export=['title','date']  #这里就是设置需要导出的字段和顺序
        self.exporter.export_item(item) 	#直接用export_item方法就好
        return item

    def close_spider(self,spider):
        self.exporter.finish_exporting()	#关闭就好
        self.file.close()	#把文件也关闭一下
```



## 关于Imagepipelines的一些用法

```python
class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

class ArtileImagePipline(ImagesPipeline):
    def item_completed(self, results, item, info):
        #这个results的是一个元组，有两个参数一个是TRUE表示是否成功，第二个是一个字典，里面有文件的路径path所以可以从里面获得路径，然后可以返回item然后可以获得路径。
        for ok,value in resutls:
            item['front_image_path']=value['path']
        image_paths=[X['path'] for ok,X in results if ok]
        if not image_paths:
            raise DropItem('failed')
        return item  #这个方法一定要return一个item
    
    def get_media_requests(self, item, info):   #这个就是用来发request的
        yield Request(url=item['front_image_url'])
```

```python
ITEM_PIPELINES = {
    'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
    'ArticleSpider.pipelines.ArtileImagePipline':301
}
IMAGES_STORE='./images'
```

在setting中还可以设置图片大小

IMAGES_MIN_HEIGHT=100

IMAGES_MIN_WIDTH=100

## FilesPipeline的一些用法

> ​	一般情况下，我们不一定是下载图片，而是下载文件，但是如果直接用Request会出现错误，因为这个东西不是专门用来下东西，对于文件判定，和一些东西不太好，采用FilePipeline才是比较好的方法

```python

#安装一些包
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

#和ImagePipeline类似，FilesPipeline也是重写两个方法
class FontPipeline(FilesPipeline):
    #这个就是用来发送请求的，默认是返回是一个Request的列表，但是我们需要请求的是一个item中的url
    def get_media_requests(self, item, info):	
        url=item['file_url']
        yield Request(url=url)

    def item_completed(self, results, item, info):	#这个就是用来在完成时候用来丢弃不用的东西
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem('failed')
        return item
```

settings中需要设置储存路劲

```python
FILES_STORE ='[PATH]'
```

- **还有几点要提一下，再用download时候有一个DOWNLOAD_WARNSIZE，这个会限制你文件下载大小，如果下大文件建议改成0，就是禁用，然后DOWNLOAD_MAXSIZE这个也会限制最大文件，默认1G，可以考虑停掉用0.**
- file_path()

file_path()方法主要是用来重命名你下载的文件和进行路径选择的，但是要记住，不能用item_completed方法，因为判断时候，会被扔掉

```python
    def file_path(self, request, response=None, info=None):
        
        #这里会在FILE SOTRE子文件夹中创建
        return '{}/{}.mp4'.format(request.meta['season'],request.meta['name'])
```



## 保存到Json文件的pipeline的写法

### 自定义方法

```python
class JsonPipeline(object):
    def __init__(self):
        self.file=codecs.open('article.json','w',encoding='utf-8') #运用codecs打开文件，防止乱码，而且不用先创建
    def process_item(self,item,spider):
        lines=json.dumps(dict(item),ensure_ascii=False)+'\n'   #dumps是将字典转化为json格式的一个东西，还有一个ensure_ascii非常重要
        self.file.write(lines)
        return item
    def spider_closed(self,spider):   #当spider关闭时候就那啥
        self.file.close()
```



## 使用pycharm调试scrapy

```python
from scrapy.cmdline import execute
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","jobbole"])
```

## 数据加入Mysql中

```python
class MysqlPipeline(object):
    def __init__(self):
    	#初始化链接的参数
        self.host='127.0.0.1'
        self.user='root'
        self.password='asd369258'
        self.db='article'
	#在打开spider打开的时候，打开数据库
    def open_spider(self,spider):
       	self.con=MySQLdb.connect(host=self.host,user=self.user,password=self.password,database=self.db,charset='utf8'\
       	,use_unicode=True)  #使用MySQLdb链接数据库生成对象
        self.cursor=self.con.cursor() #这里就是要继承cursor

    def process_item(self,item,spider):
        sql='''
            insert into article(title,date,front_image_url)
            values(%s,%s,%s)
        '''
        self.cursor.execute(sql,(item['title'],item['date'],item['front_image_url']))
        self.con.commit()  #这里一定要些commit不然出问题
```

## Item Loader的使用

首先要在Item.py文件中进行定义

```python
from scrapy.loader.processors import MapCompose   #这里是import一个处理函数
from scrapy.loader import ItemLoader				#这个是导入一个ItemLoader类，很重要，后面要继承
from scrapy.loader.processors import TakeFirst		#同样是加入一个函数
```

```python
#先定义一个类，继承ItemLoader
class Article_loader(ItemLoader): 
    default_output_processor = TakeFirst()   #设定默认的输出函数，取列表中的第一个
    
def add_some(value):   
    return value+'successful'

def date_process(value):		#这个是定义函数，记住参数是value
    date=value.strip().replace('·',"")
    try:
        date = datetime.datetime.strptime(date, "%Y/%m/%d").date()
    except:
        date = datetime.datetime.now()
    return date

class ArticleItem(scrapy.Item):    #Field可以设置参数就是input_processor和output_processor
    title=scrapy.Field(
        input_processor=MapCompose(add_some)		#这个就是处理函数，里面参数是想调用的函数，对列表每个值都使用这个处理MAP差不多的感觉
    )
    date=scrapy.Field(
        input_processor=MapCompose(date_process)
    )
    front_image_url=scrapy.Field()
    front_image_path=scrapy.Field()
```

然后在spider里面就要做工作

```python
#这里要把类进程过来，首先导入，然后继承，第一个参数就是item继承，第二个就是response
item_loader=Article_loader(item=ArticleItem(),response=response)

#接下来就是提取过程，参数第一个就是field的名字，第二个就是选择器
item_loader.add_xpath('title','//h1/t
                      text()')
item_loader.add_css('date','.entry-meta-hide-on-mobile::text')
item_loader.add_value('front_image_url',response.meta.get('front_image',""))

#这里要用load_item()方法输出一下，不然没有值
item=item_loader.load_item()

#最后还是要yield
yield item
```

## 随机User-agnet使用

在爬虫过程中，往往要用随机的头部进行请求，这时候就要一些包进行随机头部

```python
from fake_useragent import UserAgent
ua=UserAgent()

ua.chrome	#这个会直接返回一个chrome的随机头部
ua.ie	#这个就会返回IE的
ua.random	#这个直接返沪随机的
```

## setting的一些设置

```python
COOKIE_ENABLED=True	#是否禁用COOKIE，防止cookie跟踪
DOWNLOAD_DELAY=10	#这个就可以设置下载延迟,以秒为单位

```

### 多个spider使用不同的setting

非常简单，只用在spider里面加入一个参数，记住不是在类中声明时候，是在class时候之下，使用

```python
custom_settings={
    'COOKIES_ENABLED':True
}
这样就可以了，会覆盖掉默认设置
```

## selenium集成到scrapy

> - selenium集成到scrapy关键是判断什么时候用selenium
> - 如何传递cookies，在哪里初始化浏览器
> - 如何解决传递参数问题

- 首先对于初始化问题，浏览器初始化有很多种，如果是一个爬虫，可以在middleware的init的时候进行初始化，这样可以防止多次打开，因为Middleware在一开始启动爬虫的时候就会进行初始化。但是对于一个project有多个spider的时候，需要在spider的init中初始化，然后用spider的属性进行调用，这样可以一个spider对应一个selenium，方便些,下面是在Middleware初始化

  ```python
  class JufeLoginMiddleware(object):
      def __init__(self,JUFE_USERNAME,JUFE_PASSWORD):
          self.username=JUFE_USERNAME
          self.password=JUFE_PASSWORD
          self.browser=webdriver.Chrome()	#初始化了浏览器
  ```

- 对判断是否用selenium，可以使用Request传递过来的meta来判断

  ```python
  def start_requests(self):
      url='http://ecampus.jxufe.edu.cn/web/guest/student'
      
      #在meta中传递一个参数selenium设置成True
      yield Request(url=url,callback=self.parse,meta={'UseSelenium':True})
  ```

  ```python
  def process_request(self,request,spider):
      if request.meta.get('UseSelenium'):   #判断是否需要使用selenium
          
          #使用selenium登入
          self.browser.get(url='https://ssl.jxufe.edu.cn/cas/login')
          self.browser.find_element_by_id('username').send_keys(self.username)
          self.browser.find_element_by_id('password').send_keys(self.password)
          self.browser.find_element_by_xpath('//input[@type="submit"]').click()
          time.sleep(3)
  ```

- 对于登入后的cookies，可以使用meta在中间件中把selenium的cookie作为参数传回来，然后用response接收就好了

  ```python
  request.meta['UseSelenium']=False #注意要把是否用selenium的参数改掉，不然会循环的
  
  #使用get_cookies()的方法，把获取selenium的cookies
  selenium_cookies=self.browser.get_cookies()	
  request.meta['cookies']=selenium_cookies	#这里用meta传递cookies
  
  #传回response使用HtmlResponse，这里要十分注意，url一定要传，body传源码，encoding一定要写
  return HtmlResponse(url=request.url,body=self.browser.page_source,encoding='utf-8')
  ```

- 之后的请求就不用管cookie了，直接使用Request就好，cookie会自动传递，但是如果之后还是需要用selenium就需要将cookie传递到selenium中，可以用如下方法

  ```python
  cookies=response.request.cookies
  #这样就可以获得原来的cookies,然后利用meta参数，把cookie传进去。
  ```

## 利用scrapy-selenium库将selenium集成到scapy

> 使用scrapy-selenium就不需要再middleware里面进行繁琐的操作就可以简单集成。

- 首先再spider中import

```python
from scrapy_selenium import SeleniumRequest
```

- 然后要记得再setting里面进行设置，**注意SELENIUM_DRIVER_ARGUMENTS一定要是一个可迭代对象，你就算不设置任何参数，也要给我放一个空列表在那**

```python
from shutil import which

SELENIUM_DRIVER_NAME = 'chrome'	#这里是个名字，但是重要，一定要小写chrome

#首先要将chromedriver.exe加入环境变量，然后用which使用而已
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')	

#
SELENIUM_DRIVER_ARGUMENTS=[]  # '--headless' if using chrome instead of firefox

DOWNLOADER_MIDDLEWARES = {
   'scrapy_selenium.SeleniumMiddleware': 800,	#这样打开middleware
}
```

- 最后只要再spider里面请求就好，使用SeleniumRequest，里面参数主要又url，callback这种常见的，**还可以用wait_time和wait_until**

```python
yield SeleniumRequest(url=url,callback=self.get_download，wait_time=5)
```

## 暂停重重启spider

首先要在最大目录下下创建一个文件夹（不创建也可以，但是临时改不方便）

然后运行的时候

```python
#改一下启动命令就好，-s后买你JOBDIR里面等于文件的路径，这里会保存一些中间的过程，然后再次输入就是重新启动
scrapy crawl jobbole -s JOBDIR=job_info/001  

#重新开始爬取就把001改成其他就可以了
```



## from_crawler的一些用法

在Middlerware获得settings中的一些设置

```python
@classmethod
def from_crawler(cls,crawler):
    ZHIHU_USERNAME=crawler.settings.get('ZHIHU_USERNAME')
    ZHIZHU_PASSWORD=crawler.settings.get('ZHIHU_PASSWORD')
    return cls(ZHIHU_USERNAME,ZHIZHU_PASSWORD)
```

这样就让这个类中有了ZHIHU_USERNAME,ZHIZHU_PASSWORD这两个，要用__init__()来接收

```python
def __init__(self,ZHIHU_USERNAME,ZHIHU_PASSWORD):
    #获取知乎的账号密码
    self.zhihu_username=ZHIHU_USERNAME
    self.zhihu_password=ZHIHU_PASSWORD
```

## 关于不同item使用不同pipeline的用法分析

> ​	所有的item被yield后都会进入所有的pipeline，所以要想区分不同的，且process_item()中的item参数其实是一样的，所以要区分不同的item需要用isinstance（）方法。

```python
def process_item(self,item,spider):
    if isinstance(item,profitItem):
        self.exporter_profit.fields_to_export=['STOCK_NUMBER','YEAREND_DATE_PROFIT','TURNOVER','PBT','OPER_PROFIT','NET_PROF','INCOME_NETTRADING','INCOME_NETFEE','INCOME_INTEREST','EPS','DPS']
        self.exporter_profit.export_item(item)
        return item
    elif isinstance(item,assetsItem):
        self.exporter_assets.fields_to_export = ['STOCK_NUMBER','YEAREND_DATE_ASSETS', 'TOTAL_LIAB', 'TOTAL_DEBT', 'TOTAL_ASS',
                                          'OTHER_ASS', 'LOAN_TO_BANK', 'INVENTORY', 'FIX_ASS',
                                          'FINANCIALASSET_SALE', 'EQUITY', 'DERIVATIVES_LIABILITIES',
                                          'DERIVATIVES_ASSET', 'DEPOSITS_FROM_CUSTOMER', 'CURR_LIAB', 'CURR_ASS',
                                          'CASH_SHORTTERMFUND', 'CASH']
        self.exporter_assets.export_item(item)
        return item
    else:
        self.exporter_cash.fields_to_export=[
            'STOCK_NUMBER','YEAREND_DATE_CASH','CF_NCF_OPERACT','CF_INV','CF_INT_REC','CF_INT_PAID','CF_FIN_ACT','CF_EXCH',
            'CF_END','CF_DIV_REC','CF_DIV_PAID','CF_CHANGE_CSH','CF_BEG'
        ]
        self.exporter_cash.export_item(item)
        return item
```

这里就对过来item进行判断，判断他的超类是否属于items中定义的某个超类，这样就可以得到检查各种Item的效果。

## 代理使用

我发现一个好用的ip池

[p.ashtwo.cn](https://link.zhihu.com/?target=http%3A//p.ashtwo.cn/)



使用很简单，在middleware里面对process_request中改，首先要获取

```python
from pyquery import PyQuery as pq
html = pq(url="http://p.ashtwo.cn/")
ip = html('p').text()
request.meta['proxy']='http://'+ip
```

## JSONRequest

JSONRequest是新出的一个包，因为有时候你post并不是post字典或者表格，他接受的是json格式，所以这个时候就要用JSONRequest，里面的data传入字典，他会默认将你字典转化成json进行Post，非常好用