> Tushare平台免费提供不错的数据，这是初始化的用法

# 初始化接口

- 链接api，初始化接口

```python
import tushare as ts
pro=ts.pro_api('token')
```

- 对pro调用各种接口即可，这里以交易历史信息为例，具体使用看手册就好

```python
df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
```

