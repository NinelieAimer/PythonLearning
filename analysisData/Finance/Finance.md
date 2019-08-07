## 估值

> ​	各种股指都是我们金融过程中的一些非常重要的问题，使用蒙特卡洛模拟可以解决一些估值问题

### 欧式期权

欧式看涨期权到期日收益可以通过公式$h(S_{T})=\max (S_{T}-K,0)$来得出，道理都懂的，其实就是行权的收益而已。在一个完全市场中，这种权证的价格由下面公式表示
$$
C_{0}=e^{-rT}E_{0}^{Q}(h(S_{T}))=e^{-rT}\int_{0}^{\infty}h(s)q(s)ds
$$

### 美式期权

## 风险测度

### 风险价值

风险价值（VaR）使用最典型的过程，可以得到30日内的模拟，收益率。然后使用直方图表示出来。

```python
S0=100
r=0.05
sigma=0.25
T=30/365
I=10000
ST=S0*np.exp((r-0.5*sigma**2)*T
             +sigma*np.sqrt(T)*np.random.standard_normal(I))
R_gbm=np.sort(ST-S0)
plt.hist(R_gbm,bins=50)
plt.xlabel('absolute return')
plt.ylabel('frequency')
plt.grid(True)
```

![1563358326883](D:\learning\PythonLearning\analysisData\Math&Statistic\TyporaImg\1563358326883.png)

## 投资组合优化

直接上例子吧

```python
import tushare as ts

#%%初始化接口
pro=ts.pro_api('9526a2198c86fb0a72fa552f74ba1140033871f755dcd769e3134b7b')

#%%这里是得到数据
df_PA=pro.daily(ts_code='601318.SH',start_date='20180101',end_date='20190716')
df_ZX=pro.daily(ts_code='600030.SH',start_date='20180101',end_date='20190716')
df_TX=pro.daily(ts_code='600776.SH',start_date='20180101',end_date='20190716')
df_MT=pro.daily(ts_code='600519.SH',start_date='20180101',end_date='20190716')

#%%定义函数，生成总表
def set_date(x):
    x['trade_date']=pd.to_datetime(x['trade_date'])
    x.set_index('trade_date',inplace=True)
    return x['close']

#%%生成总表
df=pd.concat([set_date(df_PA),set_date(df_ZX),set_date(df_TX),set_date(df_MT)],keys=['df_PA','df_ZX','df_TX','df_MT'],axis=1)

#%%设置函数，用时间设置为索引
def sort_date(x):
    for i in x:
        i.sort_index(ascending=True,inplace=True)

#%%
sort_date([df_MT,df_TX,df_ZX])

#%%求出收益率每天的
def rate(x):
    for i in x:
        df[i+'_RATE']=df[i]/df[i].shift(1)-1
#%%
rate(['df_PA','df_TX','df_ZX','df_MT'])

#%%得到收益率表
df_RATE=df[['df_PA_RATE','df_TX_RATE','df_ZX_RATE','df_MT_RATE']]
```

下面我们假定不允许空头，我们将分配不同权重到4种证券上，我们先生成4个随机数，使其相加为1，这里有个技巧，先生成四个随机数，然后再用四个分别除以四个总和就好

```python
weights=np.random.random(4)
weights/=np.sum(weights)
```

然后就是公式了，我们收益率公式就不用多说，就是
$$
\mu=E\biggl(\sum_{I}w_{i}r_{i}\biggm)
$$
直接使用下面代码就可以求出年收益

```python
np.sum(df_RATE.mean()*weights)*559
```

最难的是方差我们先可以得出方差矩阵，然后公式是
$$
\sigma^2=\sum\sum w_{i}w_{j}\sigma_{ij}
$$
我们要使用矩阵计算来进行，使用如下公式

```python
np.dot(np.dot(df_RATE.cov()*559,weights),weights.T)
```

就可以求出组合的方差，然后我们算组合的标准差直接开根号就行了。我们用这个方法来模拟，可以画出边界线

```python
prets=[]
pvols=[]
for i in range(2500):
    weights=np.random.random(4)
    weights/=np.sum(weights)
    prets.append(np.sum(df_RATE.mean()*weights)*559)
    pvols.append(np.sqrt(np.dot(weights.T,np.dot(df_RATE.cov()*559,weights))))

prets=np.array(prets)
pvols=np.array(pvols)
```

这就求出对应的收益和风险标准差，然后作图

```python
plt.figure(figsize=(8,4))
plt.scatter(pvols,prets,c=prets/pvols,marker='o')
plt.grid(True)
plt.xlabel('volatitlity')
plt.ylabel('return')
plt.colorbar(label='Sharpe ratio')
```

![1563439699489](D:\learning\PythonLearning\analysisData\Math&Statistic\TyporaImg\1563439699489.png)

因为我这些股票平均收益率都是正的，所以我们没有负数，然后可以明显看到边界线。然后就是优化问题了。为了方便，我们建立一个函数，求组合的收益率和标准差

```python
def statistics(df,weights,time):
    '''Return repay and risk
    Parameters
    =============
    weights:array like
    ======
    
    Returns 
    ======
    pret
    pvol
    pret/pvol
    '''
    weights=np.array(weights)
    pret=np.sum(df.mean()*weights)*time
    pvol=np.sqrt(np.dot(weights.T,np.dot(df.cov*time,weights)))
    return np.array([pret,pvol,pret/pvol])
```

最优化投资组合的推到是一个约束最优化问题，所以用scipy的optimize的子库的minimize函数求解

```python
#%%
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
#%%
opts

========
fun: -2.2074783640571027
     jac: array([ 1.42197788e-01,  1.33067369e-04,  3.79905999e-01, -1.61528587e-04])
 message: 'Optimization terminated successfully.'
    nfev: 51
     nit: 8
    njev: 8
  status: 0
 success: True
       x: array([0.00000000e+00, 5.48449267e-01, 8.18025922e-17, 4.51550733e-01])
========
```

然后就可以尝试用这个来求解

```python
statistics(opts['x'],559,df_RATE)
```

## 有效边界

我们散点图，是可以画出有效边界的，即目标收益水平，波动率最小的所有投资者，所组成的点，这个要想画出来，要变的首先是weights，然后就是收益率，如果不定收益率只能取到最左边那个点。

```python
def min_func_port(weights,time,df):
    return statistics(weights,time,df)[1]
#%%
trets=np.linspace(0,0.25)
tvols=[]
for tret in trets:
    cons=[{'type':'eq','fun':lambda x:statistics(x,559,df_RATE)-tret},
          {'type':'eq','fun':lambda x:np.sum(x)-1}]
    res=sco.minimize(fun=min_func_port,x0=[0.25,0.25,0.25,0.25],args=(559,df_RATE),method='SLSQP',bounds=bnds,constraints=cons)
    tvols.append(res['fun'])
tvols=np.array(tvols)
```

