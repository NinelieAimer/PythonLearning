# Numpy学习

## 生成narray

### array()函数

> 生成数组最简单的方法就是使用array()函数

```python
from numpy import np

#直接将列表转化为array类型
arr1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
type(arr1)
```

> ​	narray对象有shape属性，可以用来查看数组的状态，多少行，多少列，多少维度。

```python
arr1.shape	#输出（2，5），两行五列
```

### zeros,ones等函数生成

> ​	一些特殊矩阵，比如0矩阵和1矩阵，可以用zeros和ones方法来生成，但是要传入一个shape量，来定义行和列

```python
arr2=np.zeros(shape=(2,2))
arr3=np.ones(shape=(3,4))
```

### arange函数使用

> ​	这个函数主要是生成列表一样的东西，但是是ndarray类型

```python
np.arange(10)
```

# ndarray的数据类型

> ​	ndarray生成时候应该是需要数据类型的，但是python非常智能，所以自动识别生成了，可以调用dtype属性来查看

```python
arr1.dtype
```

> 生成数组的时候是可以设置dtype的，方便计算

```python
#我们有一个有小数的数组，在生成ndarray类型时候，可以设置数据类型，直接取整
np.array([[1.1,1.2],[2.1,2.3]],dtype='int32')
```

常见的数据类型

| 名称       | 描述                                                         |
| :--------- | :----------------------------------------------------------- |
| bool_      | 布尔型数据类型（True 或者 False）                            |
| int_       | 默认的整数类型（类似于 C 语言中的 long，int32 或 int64）     |
| intc       | 与 C 的 int 类型一样，一般是 int32 或 int 64                 |
| intp       | 用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64） |
| int8       | 字节（-128 to 127）                                          |
| int16      | 整数（-32768 to 32767）                                      |
| int32      | 整数（-2147483648 to 2147483647）                            |
| int64      | 整数（-9223372036854775808 to 9223372036854775807）          |
| uint8      | 无符号整数（0 to 255）                                       |
| uint16     | 无符号整数（0 to 65535）                                     |
| uint32     | 无符号整数（0 to 4294967295）                                |
| uint64     | 无符号整数（0 to 18446744073709551615）                      |
| float_     | float64 类型的简写                                           |
| float16    | 半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位      |
| float32    | 单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位      |
| float64    | 双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位     |
| complex_   | complex128 类型的简写，即 128 位复数                         |
| complex64  | 复数，表示双 32 位浮点数（实数部分和虚数部分）               |
| complex128 | 复数，表示双 64 位浮点数（实数部分和虚数部分）               |

## astype（）方法转换数据类型

> ​	可以使用astype方法来转换数据类型

```python
a=np.array([1,2,3,4])
a.astype('np.float64')	#这里一定要用np.float64
```

> 也可以使用astype来把字符串转化为数字

```python
arr3=np.array(['1','2','3','4'])
arr3=arr3.astype(np.string_)
arr3.astype(np.int64)
```

## 数据结构

numpy.ndarry类专门化，*每列*使用不同的数据类型，而且这个类型还可以像切片一样

```python
dt=np.dtype([
    ('name','S'),('age','i4'),
    ('Height','f'),('Children','i4',2)
])
s=np.array([('Smith',45,1.83,(0,1))],dtype=dt)	#这里面一定是远元组，我不知道为啥
```



## Numpy的算术

> ​	**加减乘除都会对每个元素进行操作的**

```python
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[1,2,3],[4,5,6]])
arr1*arr2

====输出====
array([[ 1,  4,  9],
       [16, 25, 36]])
========================

1+arr1

======输出=======
array([[2, 3, 4],
       [5, 6, 7]])
===============
```

> ​	如果比较两个数组，会得到一个布尔类型的数组

```python
arr1=np.array([[1,3,5],[7,9,11]])
arr2=np.array([[2,4,6],[6,8,10]])
arr3=arr1>arr2	#这里用arr3来接收这个矩阵
arr3

#这里有的一点很重要，计算布尔的时候，也会与每一个值进行比较，然后会生成一个布尔矩阵

==输出====
array([[False, False, False],
       [ True,  True,  True]], dtype=bool)
=======
```

## 索引和切片

==首先，非常重要的一点，ndarray就算你切片出来赋值到一个变量上，他指向的还是原来的地址，所以你更改这个东西，会改变原来的数值，这个和列表不同==

```python
list1=[1,2,3,4]
list2=list1[1:]	#其实这里复制了一份，赋值给list2
list2[0]=3
list1
===输出==
[1, 2, 3, 4]	#这里没有改变List1
=========

arr1=np.array([[1,2,3],[4,5,6]])
arr2=arr1[:,1:]
arr2[0]=[5,6]
arr1
==输出===
array([[1, 5, 6],
       [4, 5, 6]])	#这里改了arr2，arr1也被改了
=======

#如果要复制，就用copy()赋值一份
arr1=np.array([[1,2,3],[4,5,6]])
arr2=arr1[:,1:].copy()
arr2[0]=[5,6]
arr1
```

*其实要避免这个*，可以用copy库中的deepcopy方法

```python
from copy import deepcopy
a=1
b=deepcopy(a)
```



### 索引

#### 基本索引

==因为数组中索引很重要，但是由于数组有很多个层次，使用索引时候要小心，索引也是从0开始==

> ​	索引的方法基本从上到下，最后两个是行和列，前面都是选择维度

```python
arr1=np.array([[1,2,3],[4,5,6]])
arr2=arr1[:,1:].copy()
arr2[0]=[5,6]

#选择全部的
arr1[:,0:]

#选择第一行，第二列到最后
arr1[0,1:]
```

#### 布尔索引

> ​	布尔索引需要体会，他会选出对应位置的True值，对于一位数据，就是选择行，但是二维数据都就会进行切片了

```python
names=np.array(['kirito','asuna','xilika','yuyi'])
#生成一个4行3列的数组
data=np.random.randn(4,3)
print(data)

#这里就选择一二行，然后再切片列了
print(data[(names=='kirito')|(names=='asuna'),1:])

#可以使用~在条件前进行反向选择
print(data[~(names=='kirito')])

#可以用自己来
data[data<0]
```

#### 神奇索引

> ​	这个索引和普通索引很不同，首先的不同就是==会自动复制一份出来==，因为这个东西一般是用来生成子集的，所以才会出现这个情况

- 只选择行的使用

  ```python
  #使用的原理其实就是传递一个数组进入arr[]中，然后就会选中行，并且是会排序的
  arr=np.empty((8,4))
  for i in range(8):
      arr[i]=i
  print(arr)
  
  #这里就生成了选取4，1，5行的一个子序列
  print(arr[[3,0,4]])
  ```
  
- 及要选择行，又要选择列就会非常不一样，如果类似切片就只会生成一个一维数组

  ```
  #要实现必须要
  arr[[3,0,4]][:,[0,2,1]]
  ```

#### 数轴转置和换轴

> ​	直接使用arr.T,就可以返回一个转置的数组了

```python
arr=np.array([[1,2,3],[4,5,6]])
arr.T
```

## 通用函数

### 一元通用函数

> ​	所谓一元通用函数就是numpy中封装的，可以对**一个**数组进行操作的函数，比如sqrt,exp等等
>
> **多用些numpy的方法速度更快**

```python
arr=np.arange(10)
np.sqrt(arr)
np.sin(arr)
np.sin(np.pi)
```

### 二元通用函数

> ​	所谓二元通用函数就是传入两个数组，并返回一个数组的函数，比如add,maximum

```python
arr=np.arange(10)
arr2=np.arange(start=10,stop=20)
np.maximum(arr,arr2)

#这样就会逐个比较arr和arr2中的大小，每个返回大的，输出一个矩阵
```

具体的函数直接查文档

## 使用数组进行面对数组编程

> ​	利用数组表达式来替代显式循环的方法，称为向量化

### numpy.where的使用

> ​	numpy.where就是一个If语句的向量版而已

```python
numpy.where(conda,x,y)
#这里有三个参数，第一个是条件，一定要是向量条件，比如arr>1(矩阵中元素大于一)，则用x替换，其余用y替换
#x,y可以是标量，也可以是向量，标量就是直接替换，向量的话就比较难说了，要用相同大小的矩阵来替换
```

```python
arr=np.random.randn(4,4)
np.where(arr>0,arr,1)

#这个的意思就是如果arr中元素位置大于0，就用本身不动，小于等于0的元素全部换成1
```

### 数学统计方法

> ​	对数组进行求均值或者求方差，等等。这些都可以对数组进行操作

#### 常用的方法

```python
arr.sum()	#求和
arr.mean()	#求均值
arr.min()	#求最小
arr.max()
arr.argmin()	#求最小值的位置
arr.argmax()	#求最大值的位置
arr.cumsum()	#从0开始累积和
arr.cumprod()	#从1开始元素累积和
```

这些方法里面有可选参数，==axis这个东西，就是代表对某个轴进行操作==，你选择哪个轴进行求和，运算，这样可以得到数组。

```python
arr.mean(axis=1)

===输出===
array([ 0.45174389, -0.45426997,  0.45235827,  0.21326627, -0.01287553])
#则合理会复制一个结果，然后返回要给数组
```

#### 唯一值和其他集合逻辑

> ​	还有一些集合操作

```python
np.unique(arr)	#计算x的唯一值，并且排序
np.intersectld(x,y)	#计算x和y的交集
np.unionld(x,y)	#计算x和y的并集，并排序
np.inld(x,y)	#计算x中元素是否包含在y中，返回一个布尔值数组
np.setdiffld(x,y)	#差集
np.setxorld(x,y)	#异或集
```

## 使用numpy进行文件输入和输出

> Numpy一般最多用来进行二进制文件操作，因为文本和表格，Pandas比这个好多了

Numpy输入和输出只有两大方法，==np.save，np.load==，默认数组的保存文件的格式是==.npy==，

```python
np.load('path')	#括号中就是路径
```

```python
#我们可以使用np.savez方法，将数组作为参数传递给函数，然后用于在文件中保存多个数组，并且添加索引
np.savez('file_name',a=arr1,b=arr2)

#这样过后，我们就把文件保存了，当我们读取的时候，就可以使用索引
file=np.load('file_name')
arr1=file['a']
```

## 线性代数

> ​	==这个运算在numpy矩阵里面并不是点乘==，矩阵的点乘需要用dot方法

```python
arr1.dot(arr2)
np.dot(arr1,arr2)
arr1@arr2
#这三个都是
```

> ​	==numpy.linalg是一个拥有矩阵分解的标准函数集，非常多常用函数在里面，需要的时候就摸索吧，查文档

### 伪随机数生成

> ​	numpy.random库中有很多函数可以生成样本

```python
samples=np.random.normal(size=(4,4))	#这里一定要写size，因为默认参数不是size
```

一些函数使用列表：

**这里的size就可以是要给括号数，也可以是一个数字，如果是一个数字，就是一个一维数组，对应个数**

| 函数      | 描述                                 | 例子                                                         |
| --------- | ------------------------------------ | ------------------------------------------------------------ |
| seed      | 随机数生成器，输入种子就好           | np.random.seed(12)                                           |
| rand      | 从均匀分布中抽取样本                 | np.random.rand(2,3)                                          |
| randint   | 根据给定的由低到高的范围抽取随机整数 | np.random.randint(low=2,high=10,size=(2,3),dtype='int64')，这个High不会包括，和range一样 |
| binomial  | 从二项分布中抽取样本                 | np.random.binomial(3,0.1,size=(2,3))                         |
| normal    | 从正态分布中抽样                     | np.random.normal(size=(2,2))                                 |
| beta      | 从beta分布中抽取样本                 | np.random.beta(1,2,size=(2,2))                               |
| chisquare | 从卡方分布中抽取样本                 |                                                              |

