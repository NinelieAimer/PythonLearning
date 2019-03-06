from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC

#打开网页
browser=webdriver.Chrome()
url="http://jxufe.mooc.chaoxing.com/portal"
browser.get(url)

#进入本校师生通道
wait=WebDriverWait(browser,10)
button=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'topBtn01')))
button.click()

#获取账号密码，并且点击进入
username=browser.find_element_by_id("username")
username.send_keys("2201702841")
password=browser.find_element_by_id("password")
password.send_keys("jkl147258")

#等待按钮加载
wait=WebDriverWait(browser,10)
LoginButton=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="fm1"]/table/tbody/tr[5]/td/input')))
LoginButton.click()