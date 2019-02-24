import requests
import pyquery

url='https://www.zhihu.com/explore'
headers={
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Cookie':'_zap=a8da14fb-dccb-4511-b087-72a88b2d241b; d_c0="AHChuCUwlQ6PTvtxU6RK8Fvh5vdr11TSP-A=|1543310010"; _xsrf=4Imn4OXlOMw1duz5tHqG1wUcCykFOre9; q_c1=4f17f15abf0f42838ded415d956ec121|1545007428000|1545007428000; r_cap_id="ZDIxMDJjZWMwZTU0NGQwNjg3ZmZkNTE4Y2M2ZGFmZjg=|1545007428|57c2653b3480289be925390ec9dcc4d290ea1b1d"; cap_id="M2E5NDM2OTExOWI1NDQ0MDhlY2VjNTNkNjM5NjJjZGY=|1545007428|0e88fba8ce4590c5d3840f3fe956052eeb96bbec"; l_cap_id="Yjc2ZWI0ZmVjZjBjNDFkY2IyOTU4ZmU2OTA2MTY0Y2M=|1545007428|cd088f3b132d43a1851477c2341e999b35a4958f"; capsion_ticket="2|1:0|10:1545022436|14:capsion_ticket|44:OTI2YTUzM2RmNGJkNDNjMTk5ZGRhNTFmNzFjYmNkM2Q=|987739c4710caf2fca5480996019687d1d8323d8a405626e7cee572d319dfdde"; z_c0="2|1:0|10:1545022503|4:z_c0|92:Mi4xSHNXY0JnQUFBQUFBY0tHNEpUQ1ZEaWNBQUFDRUFsVk5KN2stWEFEcnBiTDc2OEpuUkxjN1JOZzcxOVZMckYtUEZR|479186b2308ee1ede8ca4326273f4fd9f9f99b4b5f456bae9c8cd9c90e106ccf"; tst=r; tgw_l7_route=1c2b7f9548c57cd7d5a535ac4812e20e; __utma=51854390.2035424738.1545007435.1545007435.1545569041.2; __utmb=51854390.0.10.1545569041; __utmc=51854390; __utmz=51854390.1545569041.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20171122=1^3=entry_date=20171122=1'
}
r=requests.get(url=url,headers=headers)
html=pyquery.PyQuery(r.text)
items=html('.explore-tab .feed-item').items()
for item in items:
    question=item('h2').text()
    author=item('.author-link-line').text()
    file=open('test.txt','a',encoding='utf-8')
    file.write('\n'.join([question,author]))
    file.write('\n'+'='*50+'\n')
    file.close()
