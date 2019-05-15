# Jupyter notebook基础

- ctrl+c可以中断运行代码

## 有%的魔法方法，在Ipython中

- %run 可以直接运行某个文件
- %pwd可以直接获得文档所在地址

## 元组

> ​	元组是个无法改变的东西，可以拆分进行分析

```python
#在一个列表或元组中，有元组，可以用对应的东西来代表，获得
tup=[(1,2),(3,4),(5,6)]
for a,b in tup:
    print(a,b)

#但是注意，如果是一个的话，就是不一样了
for i in tup:
    print(i)
 #这个就是输出（1，2）（3，4）（5，6）
```

利用元组乘一个数字，就生成多个拷贝元组

可以利用元组的一些性质，进行数字交换

```python
a,b=3,4
b,a=a,b
print(a,b)
```

> ​	还可以用特定字符来代表后面的

```python
values=1,2,3,4,5
a,b,*rest=values
print(rest)

#这个输出是[3, 4, 5]，会生成列表
```

## datetime的一些使用方法

```python
from datetime import datetime
#使用datetime库可以引入一个datetime对象
t1=datetime(2019,4,15,20,14)  #这样可以生成一个datetime对象

#分别可以获取year,month,day
t1.year
t1.month
t1.day

#使用date(),time()可以获得date()和time()对象
t1.date()
t1.time()

#strftime方法可以把datetime对象转化为string
t1.strftime('%Y-%m-%d %H:%M')

#datetime对象之间,date()对象之间都可以加减的
t2-t1
```

## 一些方法

- sort()方法和reverse()

  ```python
  #使用sort()可以对a进行排序，默认从小到大
  a=['1','3','2','8','6']
  a.sort()
  
  #使用reverse()可以把列表倒过来排
  a.reverse()
  ```

- enumerate，这个函数是用来解决停留问题

  ```python
  #我们常常遇到这种情况，需要用索引来进行锁定元素
  i=0	#定义i索引
  for value in a:
      i+=1 #这里的i就是索引
   
  #这里我们就用enumerate()方法来循环这个列表，然后使用自带你map_test来储存索引和值
  a=['kirito','xilik','lizi']
  map_test={}
  for i,name in enumerate(a):
      map_test[i]=name
  print(map_test[0])
  ```

## zip方法的一些应用

#zip方法，可以把列表，元组相互配对，生成一个可以迭代的zip类型对象

```python
a=['time','after','time']
b=['I','am','MIKU']
zipped=zip(a,b)
for i in zipped:
    print(i) #这里就会输出3个元组('time', 'I')，('after', 'am')，('time', 'MIKU')

#还可以用元组拆分一样
for c,d in zipped:
	print(c,d)
```

## 字典的一些用法

- 使用In可以判断键是否在字典中

- 可以使用zipped的一些特性生成字典

  ```python
  a=['time','after','time']
  b=['I','am','MIKU']
  zipped=zip(a,b)
  map={}
  for c,d in zipped:
  	map[c]=d
  
  #也可以直接
  dict(zip(a,b))
  ```

- 使用hash()函数来测试一个对象是否可以作为键来使用

### 集合

集合只能用set()方法来创建，{}已经被字典占用了

- set()的一些使用

  ```python
  test=set() #创建集合对象
  
  set([1,2,3,4,4,5])#这样可以去重，生成一个集合
  ```

- 交集和并集

  ```python
  a|b #并集
  a&b #交集
  
  #可以用一些语句去交并集
  a|=b #将a和b的并集赋值给a
  a&=b #将b和a的交集赋值给a
  ```

## 列表、集合和字典的推导式

这个太重要了==半天没搞懂的东西==

### 列表推导式（集合类似就行）

```python
[expr for val in collection if condition]

#下面那就是从列表中提取出长度大于等于2的值，并且大写处理，生成列表
a=['a','bc','cde','fghi']
[i.upper() for i in a if len(i)>=2]

```

### 字典推导式

```python
[key-exper:value-exper for value in collection if condition]
a=['a','bc','cde','fghi']

#这里用enumerate来进行索引
{c:d for c,d in enumerate(a) if len(d)>=2}

#可以用zipped来做也方便
{c:d for c,d in zipped}
```

### 嵌套列表推导式

> ​	有时候有列表里面套有列表，要循环出来就要两层循环了，从外写到内部,一般两层很大了，三层就过头了，可读性会很差

```python
all_data=[['John','kirito'],['kilihaya','date']]
[name for names in all_data for name in names if name[0]=='k' or name[0]=='J']
```

## 匿名函数

```python
#匿名函数最好的就是不用写return,算完直接return
f=lambda x:x*x	#这里x是参数，可以不写的
f(3)#执行这个匿名函数，为9
```

## 生成器

这个就不多讲了，要讲一下就是推导式了，把列表的[],改成（）就好了

```python
(x**3 for x in range(10))
```

## 正则表达式

> ​	python的正则表达式是用re库来进行实现的，下面是对核心方法介绍

- compile方法，这个方法十分重要，有利于节省cpu，在数据很大时候会更好，里面有一些参数，比如flags参数，可以设置忽略大小写re.IGNORECASE

  ```python
  import re
  regex=re.compile(r'\s+')	#生成一个空格的对象
  regex.split(string)	#这个split方法比较特殊，要理解，返回一个列表
  ```

- findall方法，返回所有匹配的东西，列表

  ```python
  regex.findall(text)	#也是反的，要注意，返回一个列表
  ```

- search主要是用来**定位的**，返回一个对象，对象的一些方法很好用

  ```python
  m=regex.search(text)	#这里我们得到了一个对象
  text[m.start():m.end()]	#使用start()方法得到起始位置，end()方法得到最后位置,切片
  ```

- match只会在出现于字符串起始位置时进行匹配，如果没有匹配道就会返回None

  ```python
  regex.match(text)
  ```

- sub要传入参数，会替换匹配到的东西

  ```python
  regex.sub(new_value,text)
  ```

  

- 当我们还有**需求的时候有时候要提取匹配的一部分内容，那就是加括号了**

  ```python
  regex=re.compile(r'(te4wjlsf)@(fdsaf)')
  
  #然后匹配的时候
  m=regex.match(text)
  m.groups()	#这个是默认匹配所有，会返回一个元组，对应括号的位置
  
  #如果是findall方法，会返回一个元组列表。
  ```

