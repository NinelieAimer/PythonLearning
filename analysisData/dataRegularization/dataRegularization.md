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

- 