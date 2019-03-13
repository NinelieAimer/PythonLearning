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