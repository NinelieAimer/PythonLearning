from pyquery import PyQuery as pq
test=pq("https://www.baidu.com")
divs=test("div").items()
print(divs)
for div in divs:
    print("sf")
    print(div.text())
    break