from pyquery import PyQuery as pq
html=pq(url="https://www.taobao.com")
lis=html("li")
select=lis.find(".shell-price")
divs=select.items()
print(divs)
for i in divs:
    print(i)