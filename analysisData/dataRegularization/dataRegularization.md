# 数据规整：连接、联合与重塑

## 分层索引

> ​	分层索引所能提供的就是在更低维度的情况下处理更加高维度的数据。

- 创建一个分层索引

  ```python
  data=pd.Series(np.random.randn(9),index=[
      ['a','a','a','b','b','c','c','d','d'],
      [1,2,3,1,3,1,2,2,3]
  ])
  ===
  a  1    0.302343
     2   -0.247178
     3    0.915256
  b  1    0.383245
     3   -1.082797
  c  1   -0.212644
     2   -1.678298
  d  2   -1.073515
     3    2.350983
  dtype: float64
  ===
  #使用Index可以返回一个图，这里Levels列出了所有索引不重复的值，labels其实就是对应的编号了，估计是可以用iloc和loc选取
  data.index
  
  ===
  MultiIndex(levels=[['a', 'b', 'c', 'd'], [1, 2, 3]],
             labels=[[0, 0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 2, 0, 2, 0, 1, 1, 2]])
  ===
  ```

- 切片

  ```python
  data['b']
  data['b':'c']
  
  #这里提一下用Loc切片，其实就是高维到低维切片,先最外层，然后逐渐向内层
  data.loc['b':'c',2:3]
  ===
  b  3   -1.082797
  c  2   -1.678298
  dtype: float64
  ===
  ```

- DataFrame的每个轴都可以有分层

  ```python
  frame=pd.DataFrame(
      np.arange(12).reshape((4,3)),
      index=[['a','a','b','b'],[1,2,1,2]],
      columns=[
          ['kirito','kirito','asuna'],
          ['green','red','blue']
      ]
  )
  
  
  
  ```

  ![1557904907682](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557904907682.png)

- 每层索引都可以有名字的

  ```python
  frame.index.names=['key1','key2']
  frame.columns.names=['name','color']
  ```

  ![1557905017686](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557905017686.png)

### 重排序和层级排序

- 对层级进行排序使用swaplevel接收两个层级的序号或者层级名称，**返回新对象，原来的不变**

  ```python
  #这里只能对0轴可以，对1轴好像不行
  frame.swaplevel('key1','key2')
  ```

- 以前有sort_index的方法可以对索引进行排序，但是这里索引会有很多层级，所以有一个level参数，从0到大自己调整。

  ```python
  frame.sort_index(level=1)
  ```

  ![1557907870232](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557907870232.png)

### 按层级进行汇总统计

> ​	层级进行汇总就是按照某一层级相同的索引进行汇总

```python
frame.sum(level='key1')
```

![1557908846605](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557908846605.png)

```python
frame.sum(level='key2')
```

![1557908913364](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557908913364.png)

- 按照列进行汇总，这里插一下高维重命名列，可以用rename_axis方法，指定axis就可以了

  ```python
  frame.rename_axis({"red":"green"},axis=1)
  
  #这里的level最好就用name进行选择
  frame.sum(level='color',axis=1)
  ```

### 使用DataFrame的列进行索引

- 有时候需要把某个列或者多个列作为索引，使用set_index传入列表就可以分层索引

```python
frame.set_index(['c','d'])
```

![1557910548664](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557910548664.png)

- 默认情况下，会丢弃这两列，要想不丢弃就要用参数drop设置为False

  ```python
  frame.set_index(['c','d'],drop=False)
  ```

  

![1557910729790](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557910729790.png)

- 返回reset_index()可以将分层索引加入到列中

  ```python
  frame.reset_index()
  ```


## 联合与合并数据集

### 数据库风格的DataFrame连接

- merge函数就是用来用来做多表联合的，按照一列或者多列为键进行拼接。

  ```python
  df1=pd.DataFrame({
      'key':['b','b','a','c','a','a','b'],
      'data1':range(7)
  })
  
  df2=pd.DataFrame(
      {
          'key':['a','b','d'],
          'data2':range(3)
      }
  )
  
  pd.merge(df1,df2,on=['key'])
  ```

  ![1557927910180](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557927910180.png)

- 这个意思就是按照Key为关联进行**内部合并**，我们可以看到，**d没有了**，因为默认是取的**交集**，但是要注意，是不是会有重复的，以前data2只有3行，现在直接翻倍，因为**会统一匹配，直接重复**。

- 要想带着D，**取key的并集就要传入how参数**，默认是inner，就是取交集意思，如果我们用outer就要输入参数了。

  ```python
  pd.merge(df1,df2,on='key',how='outer')
  ```

  ![1557928494710](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557928494710.png)

- 如果列名是不同的，可以分别指定列名，这个意思其实就是lkey和rkey相等进行拼接

  ```python
  pd.merge(df3,df4,left_on='lkey',right_on='rkey')
  ```

  ![1557929096781](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557929096781.png)

- 还可以按照左边还是右边的进行拼接，这个意思就是，无论怎么样，左边的一定要有

  ```python
  df1=pd.DataFrame({
      'key':['b','b','a','c','a','b'],
      'data1':range(6)
  })
  df2=pd.DataFrame({
      'key':['a','b','a','b','d'],
      'data2':range(5)
  })
  pd.merge(df1,df2,how='left',on='key')
  ```

  

![1557931240661](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557931240661.png)

这里看，c是左边的，要加进来，data2就是空值，但是必须要有。然后就是**多对多了**，左边3个b，右边2个b，就有3*2就是6中方法组合，所以有6个b

- 使用多个键进行合并时候就传入一个列表就好。
- **==在进行列-列链接时候，传递的DataFrame索引对象会被丢弃==**

- **如果有两个相同的列，但是你拼接的时候只用了一个，另一个不会自动相等合并的，而是会加默认后缀**

  ```python
  left=pd.DataFrame({
      'key1':['foo','foo','bar'],
      'key2':['one','two','one'],
      'lval':[1,2,3]
  })
  right=pd.DataFrame({
      'key1':['foo','foo','bar','bar'],
      'key2':['one','one','one','two'],
      'rval':[4,5,6,7]
  })
  pd.merge(left,right,on='key1')
  ```

  ![1557932226491](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557932226491.png)

这个key2就被加了默认后缀，要加新的就要用suffixes参数

```python
pd.merge(left,right,on='key1',suffixes=['_left','_right'])
```

![1557932364712](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1557932364712.png)

这里就加了后缀了，对于相同的东西。

### 根据索引合并

有时候是按照索引进行合并的，有**left_index=True，right_index=True，或者都传，**来合并键。

==**来看一个经典的例子**==

```python
left1=pd.DataFrame({
    'key':['a','b','a','a','b','c'],
    'value':range(6)
})
right1=pd.DataFrame({
    'group_val':[3.5,7],
},index=['a','b'])
pd.merge(left1,right1,left_on='key',right_index=True)
```

![1558004185159](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558004185159.png)

> ​	这是一个非常经典的例子，同时用到了left_on和right_index，现在大概就知道这个意思了，**所谓left_on和left_index就是说左边按照某列或者Index来合并，和right_on，right_index就是右边按照右边表格的某个列或者索引进行匹配合并。**

### 多层索引之间合并

- 多层索引的时候就非常麻烦了，在索引上的连接是一个**隐式的多键合并**

  ```python
  left1=pd.DataFrame({
      'key1':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'key2':[2000,2001,2002,2001,2002],
      'data':np.arange(5)
  })
  
  right1=pd.DataFrame(np.arange(12).reshape((6,2)),
                      index=[['Nevada','Nevada','Ohio','Ohio','Ohio','Ohio'],[2001,2000,2000,2000,2001,2002]],
                      columns=['event1','event2'])
   
   pd.merge(left1,right1,left_on=['key1','key2'],right_index=True,how='outer')
  ```

  

![1558006961332](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558006961332.png)

> ​	这个东西看懂就好，讲有点难讲

### join方法

**join方法就是用来链接相同的索引的，用索引对应链接**

```python
left1.join(right1,how='outer')
```

### 沿轴向连接

pandas的concat函数提供了一种一致性方法来解决一些问题。**==这里可就不是left和right了，要传入列表==**

- 简单的行添加拼接

  ```python
  s1=pd.Series([0,1],index=['a','b'])
  s2=pd.Series([2,3,4],index=['a','d','e'])
  pd.concat([s1,s2])
  
  #这里仅仅是行上进行拼接，但是列上的索引是要对齐的，仅仅是因为这里的series只有一列没必要所以就没有出现空值，而且会有重复值。
  
  ====
  a    0
  b    1
  a    2		#注意这里出现了两个a，因为这个是单纯的拼接，表的结构就会出现这个问题
  d    3
  e    4
  dtype: int64
  ====
  ```

- 纵向上进行拼接，因为有时候很想纵向拼接，使用**axis=1**就好，但是这样横向索引就要一样。

  ```python
  #注意这里就默认了用how为outer，这里是join为outer,所以输出，把横向索引都出来了
  pd.concat([s1,s2],axis=1)
  ```

  ![1558009665857](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558009665857.png)

  ```python
  #我们可用join传入inner来进行,这样索引就只会取交集
  pd.concat([s1,s2],axis=1,join='inner')
  ```

  ![1558009788870](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558009788870.png)

- 如果想在连接的轴上建立一个多层索引，就要用keys参数了

  ```python
  pd.concat([s1,s2,s3],keys=['one','two','three'])
  ====
  one    a    0
         b    1
  two    a    2
         d    3
         e    4
  three  f    5
         g    6
  ====
  ```

- 在DataFrame上使用的是相同逻辑首先演示一下行上连接

  ```python
  df1=pd.DataFrame(np.arange(6).reshape((3,2)),index=['a','b','c'],columns=['one','two'])
  df2=pd.DataFrame(5+np.arange(4).reshape((2,2)),index=['a','c'],columns=['three','four'])
  pd.concat([df1,df2])
  ```

![1558010481080](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558010481080.png)

> ​	这里我故意用了列上没有对准的进行链接，看到，列如果没有对准，就会产生这个后果的

- 展示一下列的链接，顺便展示一下分层索引

  ```python
  pd.concat([df1,df2],axis=1,keys=['level1','level2'])
  ```

  ![1558010799897](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558010799897.png)

也可以传入字典来代替keys，这个可以更好理解

```python
pd.concat({df1:'level1',df2:'level2'},axis=1)
```

同样可以给分层索引取名，传入names参数就好

```python
pd.concat({df1:'level1',df2:'level2'},axis=1,names=['upper','lower'])
```

- 有时候我们在轴上进行拼接的时候，不想在这个轴上留下相同的索引，所以就需要用ignore_index参数为True，这个时候，行上的索引就会被变成0到最后数字，**这时候就不可以用分层索引了**

  ```python
  pd.concat([df1,df2],axis=0,keys=['level1','level2'],ignore_index=True)
  ```

  ![1558011511417](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558011511417.png)

### 联合重叠数据

这个主要作用就是用来填补缺失值的，就是，如果有两张表，一张有一些列缺失了，另一张没有缺失，用另一张没有缺失的来填补缺失的。**这个也是按照列来操作**

```python
df1=pd.DataFrame(
    {
        'a':[1,np.NAN,5,np.NAN],
        'b':[np.NAN,2,np.NAN,6],
        'c':range(2,18,4)
    }
)
df2=pd.DataFrame(
    {
        'a':[5,4,np.NAN,3,7],
        'b':[np.NAN,3,44,6,8]
    }
)
df1.combine_first(df2)
```

![1558012172337](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558012172337.png)

## 重塑和透视

excel里面有数据透视图，python中也可以有，将列中的东西，透视到行中，或者将行中的拆包到列中。

- stack()方法就是把列中的东西放到行里面，这个叫做堆叠，**堆叠的默认是忽略缺失值的，所以要注意**

  ```python
  data=pd.DataFrame(np.arange(6).reshape((2,3)),
                    index=['Ohio','Colorado'],
                    columns=['one','two','three'],
                    )
                    
  data.index.name='state'
  data.columns.name='number'
  
  #这样就把列放到了行上的索引上了
  data.stack('number')
  ```

  ![1558013340052](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558013340052.png)

- unstack()就是拆堆，就是把行上索引拆到列上去。默认就是拆最里面的，但是如果要拆外面的传入参数就好，从0开始是最高。

  ```python
  result=data.stack('number')
  result.unstack('state')
  ```

  ![1558014064201](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558014064201.png)

- 拆堆是可能有缺失值的

  ```python
  s1=pd.Series([0,1,2,3],index=['a','b','c','d'])
  s2=pd.Series([4,5,6],index=['c','d','e'])
  test=pd.concat([s1,s2],keys=['one','two'])
  ```

  ![1558014301714](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558014301714.png)

```python
test.unstack()
```

![1558014376908](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558014376908.png)

- 当被拆堆的时候，被拆的会变成结果中最低的层级

  ```python
  df=pd.DataFrame({
      'left':result,'right':result+5
  })
  ```

  ![1558014582504](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558014582504.png)

```python
df.unstack()
rest.columns.names=['turn','number']
```

![1558014857451](C:\Users\57206\AppData\Roaming\Typora\typora-user-images\1558014857451.png)

```python
rest.swaplevel('turn','number',axis=1)	#这里就可以换来等级，但是就是要设定axis不然出问题
```

