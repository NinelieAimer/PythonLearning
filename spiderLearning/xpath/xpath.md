注意：大部分xpath都是用列表返回值

## 准备

```python
#引入和准备工作
from lxml import etree
import  requests

url="https://www.baidu.com"
response=requests.get(url)
result=etree.HTML(response.text)    #注意这里要传入文本对象
print(result)
```

## 节点获取

### 所有节点

所有节点,值得注意的是，这里获取的全部节点，打印出来的是一个一个元素在内存中的地址的列表，每个元素是一个对象

```python
result.xpath("//*")   #获取所有节点
lis=result.xpath("//a")  #获取所有a节点
```

### 子节点和子孙节点

```python
result.xpath("//div//a")   #子孙节点就是//
result.xpath('//div/a')   #子节点只用/
```

### 父节点

```
result.xpath("//*[@id='su']/..") #这里获取了id为su的亲父节点，只有一个
```

## 属性匹配获取

```
result.xpath("//*[@class='s-manhattan-index']")  #一般都是用@获取
```

### 获取文本

```python
#文本获取就是用text()方法，但是注意是/还是//
result.xpath('//div[@id="test"]/text()')   #这里/就是一个，如果下面有子节点，是获取不到文本，只会有换行符，但是注意是用列表显示出来的
result.xpath('//div[@id="test"]//text()')  #这里//就是获取所有字节带你下面的文本，而且用列表形式显示
```

## 属性获取

属性获取直接@属性就好

```python
getattrbute=result.xpath('//*[@id="kw"]/@class') #这个也是返回列表
```

### 属性多重匹配

当属性很多的时候需要用多重匹配利用contains方法

```python
contain=result.xpath('//span[contains(@class,"btn_wr")]') #这里注意引号还有@

#xpath支持多重选择比如
contain=result.xpath('//span[contains(@class,"btn_wr") and @id="s_btn_wr"]')
```

### 按顺序选择

可以在元素后面加索引，这样就可以选择特定位置上的元素，**这里要注意的是，编号是从1开始而不是0**，具体用法查手册

### 节点轴选择

一般不会需要的，需要的时候查手册就好