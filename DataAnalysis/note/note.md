# matplotlib基本要点

## 折线图

首先是装入包

```python
from matplotlib import pyplot as plt
```

然后就是分别输入x和y的值，用数组输入

```python
x=range(2,26,2)
y=[12,13,14,15,16,17,18,19,20,15,14,16]
```

然后就可以开始绘图调用plot方法

```python
plt.plot(x,y)    分别传入x和y
```

最后可以显示出来

```
plt.show()
```

## 外观修饰

### 设置图片大小，保存图片

```python
fig=plt.figure(figsize=(20,8),dpi=80)
#一个是大小，一个是像素问题

plt.savefig("path")
#可以指定svg格式，就是矢量图
```

### 设置x轴的刻度

```python
plt.xticks(x)   #这样就把所有的x的坐标都会划到x轴上,也有yticks
plt.yticks(min(y),max(y)+1)    #注意这里不能直接y，因为y是乱序的
plt.xticks(range(2,10))  #这里就限制了一个范围步长为1，如果想让步长不一样建议用numpy
```

### 把文本放在x轴上

```python
#原理就是把x参数改为字符串的数组就好
x=["hello{}".format(i) for i in range()]
```

### 给文本设置字体

```
from matplotlib import font_manager
```

首先要找到字体的位置

然后通过

```
my_font=font_manager.FontProperties()
```



## 给图添加描述信息

```
plt.xlabel("标签名")
plt.ylabel("标签名")
plt.title("标题")
```

