
> ​	pytorch  is just a replacement for numpy to use the power of GPU , also a deep learning research platform that provide maximum flexible and speed .

## Tensor

Tensors are similar to numpy 's ndarrays ,tensors can also be used on a GPU to accelerate computing.

- Construct a randomly initalize matrix 

  - ```python
    x=torch.rand(6,3)
    y=torch.zeros(5,3,dtype=torch.long)
    z=torch.tensor([5.5,3])
    ```

    

- create a Tensor based on existing Tensor,this will reuse properties of the input tensor 

  - ```python 
    x=torch.ones(3,3,dtype=torch.float)
    y=torch.rand_like(x)
    ```

- Operations 

  - sum

  - slice

  - if you want to resize/reshape Tensor , you can use **torch .view **

  - if you want change tensor as python number you can use **.item**,but be careful  **only one tensor can be change into python number**

    ```python 
    x=torch.rand(1)
    x.item()
    ```

    

## Numpy bridge 

- coverting a torch tensor to a numpy array 

  - ```python
    a=torch.rand(5)
    b=a.numpy()
    ```

- converting numpy array to torch tensor 

  - ```python
    a=np.ones(5)
    b=torch.from_numpy(a)
    ```

    

# AUTOGRAD : AUTOMATIC DIFFERENTIATION

## preview

- if you set its attribute *.requires_grad* is *True* , it starts to track all operation  on it .you can use *backward()* and have all the gradients computed automatically .

- You can call *.detach()* to detach it from computation history , and to prevent future computation from being tracked , also you can wrap the code block in *with torch .no_grad()*

- tensor and function are interconnected  and build up an acyclic graph(非循环图)，that encodes a computation 

- if you want to compute the derivative ,you just call backward() if your tensor is a scalar ,however if you has more elements ,you have a lot to do.

  ```python
  x=torch.ones(2,2,requires_grad=True)
  y=x+2
  
  #do more operations on y
  z=y*3*3
  
  #Figure out the mean
  out=z.mean()
  
  #It is that z is just a scalar so we can use backward() to figure out derivative.
  out.backward()
  x.grad
  
  ======
  tensor([[2.2500, 2.2500],
          [2.2500, 2.2500]])
  ======
  ```
  

# All is about tensor

![image-20191112212619244](D:\learning\PythonLearning\pytorch\basic\TyporaImg\image-20191112212619244.png)

## Data Type

![image-20191112212816142](D:\learning\PythonLearning\pytorch\basic\TyporaImg\image-20191112212816142.png)

- You can use `type()` method to see the type of the object like:

```python
a=torch.randn(2,3)  
a.type()
```

- Dimension 0/rank 0(这个就是定义标量，就是一个数)

```python
torch.tensor(3.)
```

- You can use `shape` to check the dimension

```python
a.shape

==
torch.Size([2, 3])
==

#if it is a dimension 0
b.shape
===
torch.Size([])
====
```

- Dim 1/rank 1

  - You can consider this as a list

  - ```python
    #create tensor
    torch.tensor([1,2,3])
    
    ===
    tensor([1, 2, 3])
    ===
    
    #random creating a tensor
    torch.FloatTensor(3)
    
    ===
    tensor([0., 0., 0.])
    ===
    
    #from numpy
    data=np.ones(2,2)
    data=torch.from_numpy(data)
    ==
    tensor([1., 1.], dtype=torch.float64)
    ==
    ```

- You can slice the `shape` to get the size

  - ```python
    data=np.ones((2,3))
    data=torch.from_numpy(data)
    data.shape[0]
    ===
    2
    ===
    
    data.shape[1]
    ===
    3
    ====
    ```

  - You can `list` the `shape` 

    ```python
    list(a.shape)
    ```

## rand/rand_like,randin

- rand
  - create numbers between [0,1]

    - ```python
      torch.rand(2,3)
      ```

      

- rand_like

  - pass a tensor, create the tensor like the shape of the original tensor

    ```python
    a=torch.rand(3,3)
    b=torch.rand_like(a)
    ```

- rand_int(min=None,max=None,shape=None)

```python
torch.randint(2,3,(2,2))
```

- ones
- zeros
- eye
- arange

**所有后面有短下划线的上面这些方法，就是把特定矩阵转化成只含有0或者1这种，这不会返回新对象，会直接变得，小心**

```python
a,zero_()	#这样就把a矩阵全部转化为0
```







## Index

```
a=torch.randn(4,3,28,28)
a[0].shape

===
torch.Size([3, 28, 28])
===

a[0,0].shape

===
torch.Size([28, 28])
===

#like numpy index
a[:2].shape
====
torch.Size([2, 3, 28, 28])
====
```

## Operation

### View/reshape

```python
a.reshape([4,3,28*28])
```

### Squeeze v.s. unsqueeze（挤压和展开）

```python
a.unsqueeze(0).shape
==
torch.Size([1, 4, 3, 28, 28])
==

a.unsqueeze(-2).shape
==
torch.Size([4, 3, 28, 1, 28])
==
```

```python
b=torch.randn(1,1,23,1)
b.shape
===
torch.Size([1, 1, 23, 1])
===


b.squeeze(0).shape
===
torch.Size([1, 23, 1])
===
```

### Expand

![image-20191112222345794](D:\learning\PythonLearning\pytorch\basic\TyporaImg\image-20191112222345794.png)

> ​	这里只能把为1的开始扩张，如果不为**1或者-1**的要出事，这里的expand函数就是将，函数在更高维度上复制出来，但是同时**我们可以在高维度地方插入1，然后再扩展**

```python
a=torch.randn(1,4)
===
tensor([[-1.1639,  1.4806,  0.4077,  1.0021]])
===

a.expand(3,4)

===
tensor([[-1.1639,  1.4806,  0.4077,  1.0021],
        [-1.1639,  1.4806,  0.4077,  1.0021],
        [-1.1639,  1.4806,  0.4077,  1.0021]])
===

b=torch.randn(4)
====
tensor([-0.9573,  1.6805,  0.6539, -1.6508])
===

b.expand(3,4)
====
tensor([[-0.9573,  1.6805,  0.6539, -1.6508],
        [-0.9573,  1.6805,  0.6539, -1.6508],
        [-0.9573,  1.6805,  0.6539, -1.6508]])
====
```

**两个维度，左右最外面一定是两个方括号，三个维度就是三个，这样子好记**

### Expand_as

> ​	这个很有用，按照某个tensor的维度扩展，当然前提是低维度要对齐

```python
b.expand_as(a)
```



## Broadcasting

> ​	这个其实就是一个广播机制。我们在相加的时候，都是低维度先对其，然后再补充高维度，其实就是**自动调用expand方法，然后再相加或者操作**

****

- 举个简单的例子，当我们相加一个Series对象和一个DataFrame对象时候，我们会怎么办，这时候就有广播机制，相当于一个Series对象是低维度列，比如一个[3,4]DataFrame对象和[4]的Series，这个是对齐的，所以Series**自动回Expand成[3,4]**，然后相加。**其实这个是错的！！**，在默认情况下，**Series的4个数字是被认为成[4,1]**，这是因为，在数学情况下，我们很喜欢把横行竖过来。

![image-20191113220309457](D:\learning\PythonLearning\pytorch\basic\TyporaImg\image-20191113220309457.png)

Broadcasting can use to reduce comsumption of the memory.

![image-20191114220221344](D:\learning\PythonLearning\pytorch\basic\TyporaImg\image-20191114220221344.png)

这个情况发生时候，你肯定要用切片，先把第一个维度切片出来，然后再相加就可以用广播机制了。

## Merge or split

### Cat(就是pandas里面concat)

- 这个和pandas不一样地方就是有一个dim参数，这个类似于axis参数，所以不用担心，就是从高维度开始拼接。**默认是0，可以设置的**

```python
a=torch.randn(3,32,8)
b=torch.randn(4,32,8)
c=torch.cat(tensors=[a,b],dim=0)
c.shape

===
torch.Size([7, 32, 8])
===
```

- **只有在需要concat的维度不一样，其他维度一样才可以concat**

### stack

> ​	这个东西和cat的方法不一样的地方在于，这个会在你想cat的位置创建一个新维度进行拼接，这个与其说是拼接，我感觉更像是创建某种东西。这里有个前提，就是要拼接的**两个tensor都要一模一样维度特征**

```python
a=torch.randn(3,32,8)
b=torch.randn(4,32,8)

d=torch.stack(tensors=[a,b],dim=0)	#会报错，因为3和4不对齐

a=torch.randn(4,32,8)
d=torch.stack(tensors=[a,b],dim=0)
d.shape
===
torch.Size([2, 4, 32, 8])
===

```

### split

- 这个很简单的，就是在某个维度上拆分成为多个就行了

```python
c.shape
===
c.shape
===

aa,bb=c.split(split_size=[3,4],dim=0)
print(aa.shape)
print(bb.shape)
===
torch.Size([3, 32, 8])
torch.Size([4, 32, 8])
===

dd,ee,ff=c.split(split_size=[1,3,3],dim=0)	#可以多个，没关系

```

### chunk

> ​	这个和split差不多的，但是就是一开始不是tensor_size，而是一个数字，**平均分成机组**

```python
ff,gg=c.chunk(chunks=2,dim=1)
print(ff.shape,gg.shape)
===
torch.Size([7, 16, 8]) torch.Size([7, 16, 8])
===
```

## 数学运算

> ​	加减乘除，矩阵运算，和numpy基本一样，我这里着重讲一下对数

```python
a=torch.exp(torch.ones(2,2))
torch.log(a)	#默认以e为底
torch.log2(a)	#以2为底
```

- 还有就是` clamp ` 参数，这个你就把他当成把矩阵规定在某个区间里面

```python
grad=torch.rand(2,3)*15
grad.clamp(10)	#小于10的全部变成10
===
tensor([[10.0000, 10.0000, 10.4536],
        [14.4394, 10.0000, 10.0000]])
===

```

## 属性统计

#### norm

> ​	这个是范数的意思，但是由于我没有学范数，所以暂时放一放

#### mean,sum,min,max.prod

> ​	这个就太熟悉了，不多说

#### argmax,argmin

> ​	这个是获取最大值和最小值所在位置的，**注意，在不给dim参数的情况下，矩阵会被打平，就是会变成一个列表再返回索引，这显然是我们不想见到的，所以dim参数一定要传入**

```python
test=torch.tensor([[2,4,5,6],[5,6,7,9]])
print(test.argmax(),test.argmin()) 
===
tensor(7) tensor(0)
===
```

当我们想获得每行最大值位置，需要使用dim参数

```python
test.argmax(dim=1)
===
tensor([3, 3])
===
```

> ​	对于max,min方法，我们可以使用dim参数，返回一个tuple，第一个返回values，第二个就是每行索引

```python
test.max(dim=1)
===
torch.return_types.max(
values=tensor([6, 9]),
indices=tensor([3, 3]))
===
```

还有一个参数是keepdim，就是原来矩阵是二维的，我们想Max之后，仍然是二维的，就使用这个为True就好

```python
test.max(dim=1,keepdim=True)
===

torch.return_types.max(
values=tensor([[6],
        [9]]),
indices=tensor([[3],
        [3]]))
===
```

## 高阶操作

### where

> ​	这个和numpy中的是一样的

`torch.where(condition,x,y)`

```python
cond=torch.rand(2,2)
cond
===
tensor([[0.8085, 0.7105],
        [0.2334, 0.4978]])
===

a=torch.zeros(2,2)
b=torch.ones(2,2)
torch.where(cond>0.5,a,b)
===
tensor([[0., 0.],
        [1., 1.]])
===
```

## tensor的保存

> ​	很多时候，我们需要将tensor保存到文件中，直接用torch的save方法

```python
torch.save(points,'./test.t')

#读取时候
test=torch.load(f='./test.t')
```

> 还有一个方法就是使用HDF5这种numpy的格式

```python
import h5py
f=h5py.File(name='./h5_test.hdf5',mode='w')	#创建一个hdf5文件，使用w方式
f.create_dataset(name='test_hdf',data=new_data)	#创建一个数据集，使用test_hdf名字
f.close()

#读取时候
f=h5py.File(name='./h5_test.hdf5',mode='r')	#创建一个文件对象
data_obj=f['test_hdf']	#使用key来读取需要的数据集对象
data=data_obj[:,:]	#这样才能得到文件，需要选出来
```







