# 概况

本项目为一个全网上市公司的财务报表爬虫，基于scrapy框架开发，利用<http://quotes.money.163.com/hkstock>，提供的信息，爬取某个股票从2006年到2016年的财务报表信息。然后储存到CSV文件。

# 使用方法

安装scrapy框架

在settings.py中更改STOCK_NUMBER，即更改股票编号（目前仅支持一个）

运行Main.py文件

## 爬取表对应

- profit.csv====>利润表
- cash.csv====>现金流量表
- assets.csv====>资产负债表

## 各项指标对应

### 利润表

- DPS:每股派息
- EPS:每股基本盈利
- INCOME_INTEREST：利息收益
- INCOME_NETFEE：费用收益
- INCOME_NETTRADING：交易收益
- NET_PROF：净利润
- OPER_PROFIT：经营利润
- PBT：息税前利润
- TURNOVER：总营收

### 资产负债表

* CASH：现金及银行结存
* CASH_SHORTTERMFUND：库存现金及短期资金
* CURR_ASS：流动资产
* CURR_LIAB：流动负债
* DEPOSITS_FROM_CUSTOMER：客户存款
* DERIVATIVES_ASSET：金融资产
* DERIVATIVES_LIABILITIES：金融负债
* EQUITY：股东权益
* FINANCIALASSET_SALE：可供出售证券
* FIX_ASS：固定资产
* INVENTORY：存款
* LOAN_TO_BANK：银行同业存款及贷款
* OTHER_ASS：其他资产
* TOTAL_ASS：总资产
* TOTAL_LIAB：总负债

### 现金流量表

- CF_BEG：期初现金及现金等价物
- CF_CHANGE_CSH：现金及现金等价物净增加额
- CF_DIV_PAID：已派股息
- CF_DIV_REC：已收股息
- CF_END：期末现金及现金等价物
- CF_EXCH：汇率变动影响
- CF_FIN_ACT：融资活动产生现金流
- CF_INT_PAID：已付利息
- CF_INT_REC：已收利息
- CF_INV：投资活动产生现金流
- CF_NCF_OPERACT：经营活动产生的现金流

