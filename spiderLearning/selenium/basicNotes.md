## 声明浏览器

```python
from selenium import webdriver

#声明浏览器对象
browser=webdriver.Chrome()
browser=webdriver.PhantomJS()
```

## 访问页面

```python
browser.get("https://www.baidu.com")
print(browser.page_source)
browser.close()
```

## 获取节点方法

### 单个节点

selenium支持各种选择，包括xpath和css选择，也包括js里面的那种,多摸索查手册

```python
#获取这页面节点
print(browser.find_element_by_id("su"))
print(browser.find_element_by_css_selector("#su"))
print(browser.find_element_by_xpath('//input[@id="su"]'))
```

### 多个节点

多个节点就是把上面的element改成elements

返回的是列表类型

### 节点交互

```python
browser=webdriver.Chrome()
browser.get("https://www.baidu.com")
input=browser.find_element_by_id("kw")
input.send_keys("刀剑神域")
button=browser.find_element_by_id("su")
button.click()
print(browser.page_source)


send_key() #这个方法用在搜索框里面的
click() #这个是点击事件
```

### 动作链条

这个是用来拖拽等动作可以自己查询官方文档

### 执行JavaScript

```python
#JavaScript操作
browser=webdriver.Chrome()
browser.get("https://www.taobao.com")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  #这里就是js代码
```

### 获取属性

```python
#获取属性,直接用get_attribute方法
browser=webdriver.Chrome()
browser.get("http://www.baidu.com")
logo=browser.find_element_by_id("su")
print(logo.get_attribute("class"))   #记得打引号
```

### 获取特殊属性

```python
input.text   #获取文本，这里就是属性，不是方法
Input.id
input.location   #获取节点的相对位置
input.tag_name   #获取标签名称
input.size #获取节点长和宽
```

### 切换frame

因为网页有子页面，可能要切换到子页面去操作，所以switch_to.frame()

```python
from selenium.common.exceptions import  NoSuchElementException
browser=webdriver.Chrome()
url="http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to.frame("iframeResult")  #这个id要自己擦会

try:
    logo=browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print("no")
browser.switch_to.parent_frame()
logo=browser.find_element_by_class_name('logo')
print(logo.text)
```

### 延时等待

主要怕有些Ajax没有加载完直接跳了

#### 隐式等待

```python
browser=webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://www.baidu.com")
input=browser.find_element_by_id("kw")
print(input)
```

#### 显式等待

显式等待主要是用来弥补隐式等待不足，可以等特定元素加载出来再执行

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser=webdriver.Chrome()
browser.get("https://www.baidu.com")
wait=WebDriverWait(browser,10)
input=wait.until(EC.presence_of_all_elements_located((By.ID,'kw')))
```

这里要装入By,这个是用来保障条件的

WebDriberWait这个对象，用来执行until

还要用EC这个也是用来执行条件的

### 前进和后退

forward()方法

back()方法

### Cookies

```python
#cookies
borwser=webdriver.Chrome()
borwser.get("https://www.zhihu.com/explore")
print(borwser.get_cookies())   #获取所有cookies
borwser.delete_all_cookies()     #删除所有cookies
print(borwser.get_cookies())
```

### 选项卡管理

```python
import time

browser=webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.execute_script("window.open()")  #script方法打开新的选项卡
print(browser.window_handles)   #这里获取所有选项卡
browser.switch_to_window(browser.window_handles[1])   #这里切换选项卡
browser.get("https://www.taobao.com")
time,sleep(1)
browser.switch_to_window(browser.window_handles[0])
```

# 谷歌无头模式

谷歌支持开启无头模式

```
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
browser=webdriver.Chrome(chrome_options=chrome_options)
```