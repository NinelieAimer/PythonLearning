# -*- coding: utf-8 -*-
from scrapy import Selector
import requests
response=requests.get("https://www.baidu.com").text
select=Selector(text=response)
title=select.xpath("//title/text()").extract_first()
print(title)