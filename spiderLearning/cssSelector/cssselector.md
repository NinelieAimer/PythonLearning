**注意：pyquery选择出来的东西是一个不可迭代的pyquery对象，要用方法转换为可迭代的对象再进行循环**

## 初始化

```python
from pyquery import PyQuery as pq
html=pq(url="https://www.taobao.com")  #这里直接就可以初始化，非常方便，而且直接这个html就成为一个对象，可以自己调用方法
```

## 基础用法

这个就不多说了，前端写过，不过要注意到，这里返回的就不是列表而是一个对象

```python
lis=html("li")
print(lis)
print(type(lis))

#输出结果是
</li>
<li class="shell-i">
<div class="shell-img"/>
<div class="shell-text"/>
<div class="shell-subtext"/>
<div class="shell-price"/>
</li>
<li class="shell-i">
<div class="shell-img"/>
<div class="shell-text"/>
<div class="shell-subtext"/>
<div class="shell-price"/>
</li>
<li class="shell-i">
<div class="shell-img"/>
<div class="shell-text"/>
<div class="shell-subtext"/>
<div class="shell-price"/>
</li>
<li class="shell-i">
<div class="shell-img"/>
<div class="shell-text"/>
<div class="shell-subtext"/>
<div class="shell-price"/>
</li>
<li class="shell-i">
<div class="shell-img"/>
<div class="shell-text"/>
<div class="shell-subtext"/>
<div class="shell-price"/>
</li>
<li class="shell-i">
<div class="shell-img"/>
<div class="shell-text"/>
<div class="shell-subtext"/>
<div class="shell-price"/>
</li>
<li class="shell-i">
<div class="shell-img"/>
<div class="shell-text"/>
<div class="shell-subtext"/>
<div class="shell-price"/>
</li>
<li class="shell-i">
<div class="shell-img"/>
<div class="shell-text"/>
<div class="shell-subtext"/>
<div class="shell-price"/>
</li>

<class 'pyquery.pyquery.PyQuery'>
```

## 查找节点

### 子节点和子孙节点

子节点直接对对象使用find方法

```python
select=lis.find(".shell-price")
print(select)
```

子孙节点要用children()方法

```python
select=lis.children()
print(select)
```

### 父节点和祖先节点

与子节点类似父节点用parent()方法

祖先节点用parents()方法

### 兄弟节点

直接用siblings()的方法就好

## 遍历对象

因为pyquery选择出来的对象不是列表，不可迭代，需要用items()方法转化为可迭代对象再进行遍历，**但是遍历出来的对象仍然是pyquery对象**

## 获取信息

### 获取属性

利用attr()方法来获取属性,而且不能多个一起一定要遍历获取

```python
select=lis.children()
divs=select.items()
for i in divs:
	print(i.attr("class"))
```

### 获取文本

利用text()方法获取文本就可以，而且不需要遍历，但是每个都是用空格隔开，如果还想获取HTML，可以用HTML方法，这个要遍历的

### 伪类选择器

和JQuery一样，要的时候查文档