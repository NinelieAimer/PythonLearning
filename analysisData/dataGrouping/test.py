import requests
import json
f=requests.get('http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol=sh601288&scale=5&ma=5&datalen=10')
for i in f.text:
    print(i)
