import requests
import re
import json
def get_one_page(url):
    headers={
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    response=requests.get(url=url,headers=headers,timeout=30)
    if response.status_code==200:
        return response.text
    else:
        return None

def parse(html):
    pattern=re.compile(r'''<dd>.*?board-index.*?>(\d+)</i>.*?title="(.*?)".*?data-src="(.*?)".*?"star">(.*?)</p>.*?"releasetime".*?>(.*?)</p>''',re.S)
    items=re.findall(pattern=pattern,string=html)
    for item in items:
        yield {
            'index':item[0],
            'name':item[1],
            'img':item[2].strip(),
            'star':item[3].strip(),
            'time':item[4]
        }

def write_to_file(content):
    with open("test.txt","a",encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False,indent=5)+"\n"+"\n")

def main(offset):
    url='https://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    for item in parse(html=html):
        write_to_file(item)

if __name__=="__main__":
    try:
        for i in range(10):
            main(offset=i*10)
    except:
        print("爬取异常")