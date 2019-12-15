# Summary

这是利用回归的总结，需要注意的地方

## 关于OLS

使用时候的结果参数

```python
#SST,SSE,SSR,beta
#Be careful the result is just a feature is not callable
sst=result.centered_tss
sse=result.ess
ssr=result.ssr
beta=result.params
# #Mean squared error of the residuals
sigma=result.mse_resid
confidence_interval=result.conf_int()   #confidence interval
t=result.tvalues
```

这里要注意的是**这里的params就是beta，但是是一个series对象，所以是有索引的，索引就是那些x的名字**

## 关于Pytorch的梯度算法

- 有时候需要将tesor的数据进行转换直接是用$.数据类型()$进行转换