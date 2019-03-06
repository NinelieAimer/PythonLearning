from selenium import webdriver
#
# #声明浏览器对象
# browser=webdriver.Chrome()
#
# #访问页面
# browser.get("https://www.baidu.com")
# print(browser.page_source)
#
# #获取这页面单个节点
# print(browser.find_element_by_id("su"))
# print(browser.find_element_by_css_selector("#su"))
# print(browser.find_element_by_xpath('//input[@id="su"]'))
#
# #获取多个节点
# a=browser.find_elements_by_css_selector("#u_sp a")
# print(a)
# print(type(a))
# browser.close()
#
# #节点交互
# browser=webdriver.Chrome()
# browser.get("https://www.baidu.com")
# input=browser.find_element_by_id("kw")
# input.send_keys("刀剑神域")
# button=browser.find_element_by_id("su")
# button.click()
# print(browser.page_source)

#JavaScript操作
# browser=webdriver.Chrome()
# browser.get("https://www.taobao.com")
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#获取属性
# browser=webdriver.Chrome()
# # browser.get("http://www.baidu.com")
# # logo=browser.find_element_by_id("su")
# # print(logo.get_attribute("class"))   #记得打引号
# # print(logo.location)

#切换iframe
import time
# from selenium.common.exceptions import  NoSuchElementException
# browser=webdriver.Chrome()
# url="http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame("iframeResult")
#
# try:
#     logo=browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print("no")
# browser.switch_to.parent_frame()
# logo=browser.find_element_by_class_name('logo')
# print(logo.text)

#延时等待
#隐式等待
# browser=webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get("https://www.baidu.com")
# input=browser.find_element_by_id("kw")
# print(input)

#显示等待
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser=webdriver.Chrome()
# browser.get("https://www.baidu.com")
# wait=WebDriverWait(browser,10)
# input=wait.until(EC.presence_of_all_elements_located((By.ID,'kw')))

# #cookies
# borwser=webdriver.Chrome()
# borwser.get("https://www.zhihu.com/explore")
# print(borwser.get_cookies())
# borwser.delete_all_cookies()
# print(borwser.get_cookies())

#选项卡管理
# import time
#
# browser=webdriver.Chrome()
# browser.get("https://www.baidu.com")
# browser.execute_script("window.open()")
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get("https://www.taobao.com")
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
