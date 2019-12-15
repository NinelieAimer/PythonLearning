# 逼近法

首先我们可以画出图像，使用numpy的linspace，这个就是生成一个等差数列，参数为start,end,个数，默认取50个，可以自己设置

```python
#逼近法
def f(x):
    return np.sin(x)+0.5*x

#%%
x=np.linspace(-2*np.pi,2*np.pi,50)

#%%
plt.plot(x,f(x),'b')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
```

可以得到如下图

![1562661404943](D:\learning\PythonLearning\analysisData\Math&Statistic\TyporaImg\1562661404943.png)

## 回归分析

> pandas已经不能做回归，一定用statsmodel或者numpy的一些包做

### 作为基函数的单项式

> 最简单的情况基本都是用单项式，也是最简单的，一次式，二次式，三次式都是指最高次数为多少的式子，我们常用的最小二乘法回归分析，基本都是一次式。

使用numpy进行回归分析，最重要的两个函数就是polyfit和polyval，第一个是用来算相关系数$\rho$，然后用polyval($\rho$,x)返回用x的回归值。我们看一下polyfit的一些参数,**注意这个只能算出$\rho$要算回归的要用polyval**

| 参数 | 描述                     |
| ---- | ------------------------ |
| x    | x坐标                    |
| y    | y坐标                    |
| deg  | 这个是最高项次数         |
| full | 如果为真，返回额外的信息 |
| w    | 应用到y坐标的权重        |
| cov  | 如果为真，返回协方差矩阵 |

我们来做一个简单的一元线性回归

```python
#%%
rho=np.polyfit(x,f(x),deg=1)	#这个意思就是拟合，然后deg代表一次式，算出rho
y=np.polyval(rho,x)			#这个就简单了，用rho和x算出y

#%%
plt.plot(x,y,'yo')	#这个作图就好
plt.plot(x,f(x))
```

![1562673140861](D:\learning\PythonLearning\analysisData\Math&Statistic\TyporaImg\1562673140861.png)

我们可以考虑来个五次的，用其实就是泰勒展开，就是这个，可以适当加一下图例

```python
rho=np.polyfit(x,f(x),deg=5)
y=np.polyval(rho,x)
plt.plot(x,y,'yo',label='regression')
plt.plot(x,f(x),label='f(x)')
plt.legend(loc='best')	#这里可以了解一下,添加图例，直接用一个图，我们不用子图
```

![1562673193820](D:\learning\PythonLearning\analysisData\Math&Statistic\TyporaImg\1562673193820.png)

我们还可以用一个函数进行检验一下

```python
np.allclose(f(x),y)
====
False	#返回False，说明拟合效果还不是很好
===
```



当然还有更好的选择，就是用statsmodel进行操作。

```python
x=sm.add_contant(x)	#这个是把x转化未有截距的东西，就是能够有aphla
model=sm.OLS(y,x).fit()
model.summary()
```

![1563105307322](D:\learning\PythonLearning\analysisData\Math&Statistic\TyporaImg\1563105307322.png)

这样就可以得出一个表，详细信息，需要详细学习统计学才可以分析好。

```python
plt.plot(x,model.predict(),'yo')
plt.plot(x,f(x))
```

![1563105452840](D:\learning\PythonLearning\analysisData\Math&Statistic\TyporaImg\1563105452840.png)

### 多元回归

> ​	我个人都还不会多元回归这个东西，也没用过，所以先放着不学了

### 插值

> ​	插值是一种通过已知的、[离散](https://zh.wikipedia.org/wiki/離散)的[数据](https://zh.wikipedia.org/wiki/数据)点，在范围内推求新数据点的过程或方法。与回归相比，插值主要是给定一组有序的观测点，基本思路就是在两个相邻数据点之间进行回归，不仅可以产生的分段插值函数完全匹配数据点，而且函数在数据点上连续可微。连续可微性需要至少三阶插值。

- 首先导入子库

```python
import scipy.interpolate as spi
x=np.linspace(-2*np.pi,2*np.pi,25)
```

- 我们还是用原来的函数来试一下

```python
def f(x):
    return np.sin(x)+0.5*x
```

- 然后就是使用方法了，类似于polyfit和polyval这种函数，有splrep和splev，下面是isplrep

| 参数        | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| x           | x坐标                                                        |
| y           | y坐标                                                        |
| w           | 用在y上的权重                                                |
| xb,xe       | 拟合区间，如果设置为None则区间为[x[0],[-1]]，其实就是整个区间长度 |
| k           | 样条拟合顺序                                                 |
| s           | 平滑因子                                                     |
| full_output | 如果为真，返回附加输出                                       |
| quiet       | 如果为真，抑制消息                                           |

- splev函数的参数

| 参数 | 描述                            |
| ---- | ------------------------------- |
| x    | x坐标                           |
| tek  | splrep返回的长度为3的序列       |
| der  | 导数的阶(0为原函数,1为一阶导数) |
| ext  | 如果x不在节点序列中时的行为     |

我们试着做一下

```python
plt.plot(x,f(x),'b',label='f(x)')
plt.plot(x,iy,'r.',label='interpolation')
plt.legend(loc='best')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
```

![1563156303959](D:\learning\PythonLearning\analysisData\Math&Statistic\TyporaImg\1563156303959.png)

然后可以用数值化方式加以确认

```python
np.allclose(f(x),iy)
```

- **样条插值**在金融学中往往用于估算未包含在原始观测点中的自变量数据点的因变量的值，为此，我们选择一个更小的区间，观察一下

```python
xd=np.linspace(1.0,3.0,50)
iyd=spi.splev(xd,ipo)
plt.plot(xd,f(xd),'b',label='f(x)')
plt.plot(xd,iyd,'r.',label='interpolation')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
```

![1563156764508](D:\learning\PythonLearning\analysisData\Math&Statistic\TyporaImg\1563156764508.png)

看起来拟合并不是特别好，所以我们用k=3算ipo试试

![1563156843717](D:\learning\PythonLearning\analysisData\Math&Statistic\TyporaImg\1563156843717.png)

看起来非常棒，但是用np.allclose并不完美，但是MSE确实小，其实就是方差了

> ​	在可以应用样条插值的情况下，可以预期比最小二乘回归方法更好的近似结果。但是要记住**必须要有序的无噪声数据**

# 凸优化

> ​	凸优化感觉起来就是找最大最小值的一种算法感觉

- 我们先用一个函数来举例子，这里要**尤其要注意**，python3已经不支持传入元组数据，所以要像下面那样定义函数

```python
def fm(z):
    x,y=z
    return (np.sin(x)+0.05*x**2+np.sin(y)+0.05*y**2)

x=np.linspace(-10,10.50)
y=np.linspace(-10,10,50)
x,y=np.meshgrid(x,y)
z=fm((x,y))
```

这是一个三维函数，可以通过图像看出来，然后我们打算实施全局最小化和局部最小化的方法来找到最小值。使用brute和fmin函数

## 全局优化

> ​	就是在全局范围内寻找最大最小值的感觉，没有什么感觉，可以按照函数来进行凸优化使

- 我们先来看一个寻找全局最小值的

```python
import scipy.optimize as spo

#使用brute函数，这里参数第一个是函数，就是要优化的函数，第二个是区间，这里区间这样写，注意看
opt1=spo.brute(fm,((-10,10.1,0.1),(-10,10.1,0.1)),finish=None)	
```

- 然后我们输出一下

```python
fm(opt1)	#这里就求出了最小值，但是是近似的，并不是非常精确，可以用局部优化去求更加精确的
```

## 局部优化

> ​	局部优化感觉就在一个邻域内寻找最小值感觉，一般都是用在全局优化后更加优化时候使用

- 使用fmin可以做到局部优化，参数第一个func不说了；第二个x0是估测的值，一般都需要用全局优化来算出来；arg这个是其他需要传入函数的参数；xtol是波动幅度意思，指自变量的波动幅度；ftol指函数的波动幅度，每次迭代时候。maxiter最大迭代次数，maxfun函数最大调用次数

```python
opt2=spo.fmin(func=fm,x0=opt1,xtol=0.001,ftol=0.001,maxiter=15,maxfun=20)
opt2

====
array([-1.42702972, -1.42876755])
====

#我们找到更加优的解
```

## 有约束的优化

> ​	在金融中，多半都是有约束条件的优化问题的，我们来进行一个例子

- 使用scipy.optimize.minimize进行解决问题，先定义一个函数

```python
def Eu(z):
    s,b=z
    return -(0.5*np.sqrt(s*15+b*5)+0.5*np.sqrt(s*5+b*12))
```

- 我们介绍一下minimize这个函数，第一个参数func不讲；第二个参数x0是估测值，是指的函数输入参数的初始值，估测值；method这个参数是使用什么求解器，即使用什么算法进行求解，因为金融多半是多变量的，而且是很多边界，等式和不等式，所以一般都用**SLSQP**，所以后面的参数就是仅仅对于SLSQP方法才有的了。bounds参数，这个参数就是一个范围参数，一定要传入**tuple**，如果是二元的，就看例子；constraints这个是对于不等式和等式的参数，**注意等式时候，要把等式转化为等于0，不等式的时候要把不等式转化为大于0**

```python
#%%
def Eu(z):
    s,b=z
    return -(0.5*np.sqrt(s*15+b*5)+0.5*np.sqrt(s*5+b*12))

#%%
cons=[{'type':'ineq','fun':lambda z:100-z[0]*10-z[1]*10}]	#这个就是字典列表,一个不等式或者一个等式一个字典，里面两个参数，一个是type,一个是fun
bnds=((0,1000),(0,1000))	#这里要这样定义范围

#%%
result=spo.minimize(fun=Eu,x0=[5,5],method='SLSQP',bounds=bnds,constraints=cons)
#%%
result
```

```
   ==========
   fun: -9.700883611487832
     jac: array([-0.48508096, -0.48489535])
 message: 'Optimization terminated successfully.'
    nfev: 21
     nit: 5
    njev: 5
  status: 0
 success: True
       x: array([8.02547122, 1.97452878])
```



这个例子不够，我们再来一个例子

```python
def statistics(weights,time,df):
    '''
    Use params to calculate the best weights
    :param weights: weights for every assets
    :param time: 
    :param df: return rate
    :return: rate
    '''
    weights=np.array(weights)
    pret=np.sum(df.mean()*weights)*time
    pvol=np.sqrt(np.dot(weights.T,np.dot(df.cov()*time,weights)))
    return np.array([pret,pvol,pret/pvol])
#%%
import scipy.optimize as sco

#%%
def min_func_sharpe(weights,time,df):
    return -statistics(weights,time,df)[2]
#%%
bnds=tuple((0,1) for x in range(4))
cons=({'type':'eq','fun':lambda x:np.sum(x)-1})
#%%
opts=sco.minimize(fun=min_func_sharpe,x0=[0.25,0.25,0.25,0.25],method='SLSQP',args=(559,df_RATE),bounds=bnds,constraints=cons)
```

通过这个例子，我们可以更加深入理解这个问题，首先是，**我们的优化仅仅是对函数的第一个参数进行优化**，第一个参数可以是一个元组，数组等等，我们的**constraints里面构造的函数中的参数是仅针对我们第一个参数进行**的。然后后面的**参数要通过args参数进行传入**。

****

**我们还可以使用pulp库进行约束优化，下面做个演示**

例子：

我们考虑两种证券X和Y，试求$3x+2y$的最大值，限制条件如下

- 2倍的X证券数量与投资Y证券数量不超过90
- 投资X证券数量与投资Y证券数量之和不超过80
- 投资X数量不超过40
- 不能卖空

```python
x=pulp.LpVariable('x',lowBound=0,upBound=40)	#初始化变量，下限和上限
y=pulp.LpVariable('y',lowBound=0)

#初始化problem,第一个name是这个模型的描述，第二个sense是选择求最大还是最小值
problem=pulp.LpProblem(name='A simple model with 2 variables',sense=pulp.LpMaximize)

problem+=3*x+2*y,'The objective function'
problem+=x+y<=80,'1st constraint'
problem+=2*x+y<=100,'2nd constraint'
stats=problem.solve()	'solve the problem'

problem   'output the result'

#see the result variables
pulp.value(x)
pulp.value(y)
```



# 积分

> ​	积分很重要的一环，可以使用**scipy.integrate**这个库来进行数值积分运算

直接上例子，我们来求一下下面函数的积分
$$
\int_{0.5}^{9.5}\sin x+0.5xdx
$$


- 我们先试一下高斯求积，使用fix_quad方法

```python
a=0.5
b=9.5
sci.fixed_quad(func=f,a=a,b=b)	#基本上积分都是第一个函数，第二个下限，第三个上限这些参数

====
(24.366995967084602, None)	#这里返回一个元组，第一个是值，第二个不知道是啥
====
```

- 还有各种积分，包括普通的quad积分，romberg积分，这些看文档就好，需要时候去找，让我们提一下无穷和多重积分
- 对于无穷范围积分，其实很简单，**就是把上限和下限变为np.inf这个无穷值就好了**

- 我们重点看一下二重积分**dblquad**方法，举个例子，我们求下面方程的积分

$$
I=\int_{y=0}^{\frac12}\int_{x=0}^{1-2y}xydxdy
$$

```python
sci.dblquad(func=lambda x,y:x*y,a=0,b=0.5,gfun=lambda x:0,hfun=lambda y:1-2*y)
```

第一个参数被积函数，第二个和第三个参数分别是确定边界，就是最外面的范围，后面就是第二层范围，但是要注意**第二层的所有上下限，都要用函数来表示**

# 符号计算

> ​	很多时候需要进行符号计算，我们有专门的符号库是**SymPy库**

```python
import sympy as sy
```

## 基本知识

> ​	引入新的对象类，最基本的是Symbol类

```
x=sy.Symbol('x')
y=sy.Symbol('y')
type(x)

====
sympy.core.symbol.Symbol
====
```

- 我们可以通过sy.simplify()对等式进行化简，前提是里面的符号要是定义的符号对象

```python
f=x**2+3+0.5*x**2+3/2
sy.simplify(f)	#用后直接化简
```

- sy的pretty功能可以很好的可视化一下公式，使用的latex的渲染，非常不错，可以用来检查公式使用

```python
sy.pretty(sy.sqrt(x)+0.5)
```

## 解方程

> ​	SymPy可以解方程，同样要保持等于0的式子，是用sy.solve进行求解

```python
sy.solve(x**2-1)

====
[-1, 1]
====
```

- 解多个未知数的方程，这里第一个参数是**一个式子或者一个可迭代的式子数组**，第二个参数也是一个可迭代的未知数的列表或者数组。我们举个例子求下面式子的解

$$
\begin{cases}
2x-y+3=0\\
3x+y-7=0
\end{cases}
$$

```python
sy.solve([2*x-y+3,3*x+y-7],*[x,y])

===
{x: 4/5, y: 23/5}
===
```

这里要注意**后面参数传入的方式前面要加\***

## 积分和微分

> ​	这个不多介绍了，直接用scipy方法更加好

# 推断统计学

## 随机数生成

> ​	这个不多说，自己查表，想生成啥，就用numpy生成数组就好了

## 模拟

> ​	蒙特卡洛模拟是金融中最重要的数值技术。所以要重点讲一下模拟

### 随机变量

这里我们举个例子，用今天的股价水平$S_{0}$来预测未来某个日期T的股票指数水平$S_{T}$，公式如下，这是著名的Black-Scholes-Merton公式
$$
S_{T}=S_{0}\exp\big((r-\frac12\sigma^{2})T+\sigma\sqrt{T}z\bigm)
$$
这个公式中r是无风险利率，$\sigma$是收益的标准差。我们用这个来一个模拟

```python
S0=100
r=0.05
sigma=0.25
T=2.0
I=10000 #number of random draws
ST1=S0*np.exp((r-0.5*sigma**2)*T
              +sigma*np.sqrt(T)*np.random.standard_normal(I))	#这里会生成一个数组，然后我们看一下分布
```

```python
plt.hist(ST1,bins=50,color='orange')
plt.xlabel("index level")
plt.ylabel("frequency")
plt.grid(True)
```

![1563262748542](D:\learning\PythonLearning\analysisData\Math&Statistic\TyporaImg\1563262748542.png)

### 随机过程

> ​	这个问题，我们暂时不过多介绍了，因为我们没有学过，记住代码没有什么意义，等以后需要时候继续学习。

#### 几何布朗运动





