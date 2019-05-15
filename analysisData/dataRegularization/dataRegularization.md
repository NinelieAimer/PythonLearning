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

  