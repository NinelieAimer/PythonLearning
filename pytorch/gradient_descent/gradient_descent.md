# 激活函数

## sigmoid

- 其实就是logistic回归里面的函数，式子是
  $$
  f(x)=\sigma(x)=\frac{1}{1+e^{-x}}
  $$
  
- 这个函数在小于0主要是0，大于0就是1，这样就可以把数值映射到（0，1）的区间。

- 而且他的导数是
  $$
  \sigma'(x)=\sigma(x)-\sigma^2(x)
  $$
  

## Tanh

$$
f(x)=tahn(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}=2sigmoid(2x)-1
$$

# Topic Loss

- Mean Squared Error(均方差，其实就是计量中的SST)

$$
\sum(y-\bar{y})^2
$$

- Cross Entropy Loss
  - binary
  - multi-class
  - **+softmax**
  - Leave it to Logistic Regression Part

## 两种求导方法

### torch.autograd.grad

这个方法，第一个参数是损失函数，第二个是参数

```python
x=torch.ones(1)
w=torch.full([1],2)
mse=F.mse_loss(torch.ones(1),x*w)	#这个是用mse函数

torch.autograd.grad(mse,[w])  #第一个是函数，第二个是需要求导的变量
#会报错，因为没有设置追踪w,而且这里要用列表，就是需要求导列表

w.requires_grad_()	#这个可以更新w,使得w可以求导

torch.autograd.grad(mse,w)  #仍然报错，因为他没有更新函数，mse要更新才可以，pytorch是一步一步更新的

mse=F.mse_loss(torch.ones(1),x*w)
torch.autograd.grad(mse,w)

===
(tensor([2.]),)
===
```

### loss.backward

使用这个可以知道，就会对使用grad的参数求导，然后使用.grad就可返回

```python
mse=F.mse_loss(torch.ones(1),w*x)
mse.backward()
w.grad

===
tensor([2.])
===
```

### Softmax

![image-20191209225037022](D:\learning\PythonLearning\pytorch\gradient_descent\TyporaImg\image-20191209225037022.png)

这个是把数据压缩到，0到1，有点像测度变换一样的东西。

可以把大的更加大，小的会压得更加紧

- 记住在求导时候，**loss一定是一个值，就是一个标量**

- 我们有三个输入$a_0,a_1,a_2$ ，然后又三个输出$p_0,p_1,p_2$ ，用p对三个求导可得
  $$
  \frac{\partial p_i}{\partial a_j}
  $$
  这个东西就需要注意，每个P对每个a进行求导，要考虑是否求导i和j是否相等。

- 当i=j时

  - $$
    \frac{\partial p_i}{\partial a_j}=p_i(1-p_j)
    $$

    

- 当$i\not=j$时

  - $$
    \frac{\partial p_i}{\partial a_j}=-p_ip_j
    $$

- 所以，一定要注意，**当$i=j$时候，导数正数，当$i\not=j$时候，导数是负数**

```python
p=F.softmax(a)
a=torch.rand(3,requires_grad=True)

p.backward()    #这里p是一个向量，是无法用来求导的，会报错


p=F.softmax(a,dim=0)
torch.autograd.grad(p[2],a,retain_graph=True)	#这个retain_graph是保存图，不被删，可以求多次导数

torch.autograd.grad(p[1],a,retain_graph=True) #求p2的导数

==
(tensor([-0.1029,  0.2287, -0.1258]),)	#注意第二个为正
==
```



# 感知机模型

![image-20191210171754016](D:\learning\PythonLearning\pytorch\gradient_descent\TyporaImg\image-20191210171754016.png)

- 这个就是单层的感知机模型，中间只有一个隐平面，而且隐平面上只有一个节点

## 术语

- 首先notation
  - $X_j^i$的意义
    - 上标为i，意思就是第几层，因为是输入层，所以永远第0层
    - 下标为j，说明0层有n个节点，所以所以是1到n
  - $W_{ab}^i$ 的意义
    - i，代表与哪一层链接，这里是第一层，所以都是1
    - a，代表与上一层哪个元素链接
    - b，与这一层的那个节点链接，因为这一层只有1个节点，所以就是0
  - 加权求和后的$X_i^j$
    - j表示第几层，这里是第一层（加上输入层就是第二层）
    - i表示第几个，这里是第一个节点，所以只有0
  - $O_i^j$
    - j代表第几层，这里第一层（加上输出第二层）
    - i是表示节点位置，就是第一个节点

## Derivative

### 单层感知机，一个节点

- 首先我们计算loss，我们用公式表示

$$
E=\frac{1}{2}(O_0^1-t)^2
$$

这个**我们这里是单个的，所以我们不需要求和符号，正常情况下是要求和的**
$$
\begin{align}
\frac{\partial E}{\partial W_{j0}}&=(O_0^1-t)\frac{\partial O_0}{\partial W_{j0}}\\
&=(O_0-t)\frac{\partial \sigma(x)}{\partial W_{j0}}\\
&=(O_0-t)\sigma(x_0)(1-\sigma(x_0))\frac{\partial X_0^1}{\partial W_{j0}}\\
&=(O_0-t)O_0(1-O_0)x_{j}^0
\end{align}
$$
所以我们总结一下
$$
\frac{\partial E}{\partial w_{j0}}=(O_0-t)O_0(1-O_0)x_j^0
$$
可以使用pytorch来模拟

```python
import torch
x=torch.randn(1,10)
w=torch.randn(1,10,requires_grad=True)

o=torch.sigmoid(x@w.t())
from torch.nn import functional as F

loss=F.mse_loss(torch.ones(1,1),o)
loss.backward()

w.grad
```

### 单层感知机，多个节点

我们感知机一般情况下都是多层的，我们推导一下多层感知机求导过程

![image-20191210221823003](D:\learning\PythonLearning\pytorch\gradient_descent\TyporaImg\image-20191210221823003.png)

我们以求$W_{jk}^1$导数为例子
$$
\begin{align}
E&=\frac{1}{2}\sum(O_i^1-t_i)^2\\
\frac{\partial E}{\partial w_{jk}}&=(O_k^1-t_k)\frac{\partial O_k}{\partial w_{jk}}
\\
&=(O_k^1-t_k)\frac{\partial \sigma(X_k)}{\partial w_{jk}} \\
&=(O_k^1-t_k)\sigma(X_k)(1-\sigma(X_k))\frac{\partial X_k}{\partial w_{jk}}\\
&=(O_k^1-t_k)\sigma(X_k)(1-\sigma(X_k))x_j^0
\end{align}
$$

- 注意这里的$w_{jk}$的意思就是，**一条线**，所以在求导第二步只有在$O_k$的情况下才有这个节点，**求和就没了**
- 最后结果和一个节点很像，但是又不一样，$w_{jk}$相关的及时一个在j，代表小$x_j^0$，k代表后面1层节点$X_k$和后面的$O_k$相关，所以本质上就是链接的一条线。

```python
x=torch.randn(1,10)
w=torch.randn(2,10,requires_grad=True)

o=torch.sigmoid(x@w.t())

loss=F.mse_loss(torch.ones(1,2),o)
loss.backward()

w.grad
```

- 这里第一个要注意的，就是w.grad的生成矩阵肯定和原来w的维度是一模一样的，**不这样怎么采用梯度下降呢**，所以这样更新梯度原理基本出来了。

### 多层感知机梯度推导

多层感知机比单层感知机不同的地方在于，如何在新的地方



