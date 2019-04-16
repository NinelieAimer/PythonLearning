# Numpy基础

## 生成数组

```python
my_array=np.array([0,1,2,3])
print(my_array)
```



## 索引和修改

```python
print(my_array[0])
my_array[0]=15
print(my_array[0])
```

## 创建一个五个元素且全为0的数组

```python
my_new_array=np.zeros((5))
print(my_new_array)
```

## 创建一个随机数组

```python
my_random=np.random.random((5))
print(my_random)
```

## 创建一个二维数组

```python
my_two=np.zeros((2,3))    #创建两行三列的意思
print(my_two)
```

## 二维数组的索引

```python
my_array2=np.array([[2,3,5],[4,5,6]])   #这里要注意外面要加中括号
print(my_array2[0][2])            #这里要注意，索引初始值为0
print(my_array2.shape)      #shape属性可以查看数组的情况，两行三列
print(my_array2[:,2])     #提取第二列的值，用冒号代替行号，类似于通配符，然后列就行
```

## 一些运算

```python
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
sum=a+b
difference=a-b
product=a*b   #这个不是矩阵乘法，仅仅是各个元素相乘
chu=a/b
juzhenchengfa=a.dot(b)    #矩阵乘法
print(sum,"\n",difference,"\n",product,"\n",chu,"\n",juzhenchengfa)
```