from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

#打开浏览器并进行登录
def get_source():
    yourUsername="2201702841"
    YourPassword="jkl147258"
    studentNumber=yourUsername[2:5]+yourUsername[-4:]
    browser=webdriver.Chrome()
    url="https://ssl.jxufe.edu.cn/cas/login"
    browser.get(url)
    wait=WebDriverWait(browser,10)
    button=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="fm1"]/table/tbody/tr[5]/td/input')))
    try:
        username=browser.find_element_by_id("username")
        username.send_keys(yourUsername)
        password=browser.find_element_by_id("password")
        password.send_keys(YourPassword)
        button.click()
    except:
        print("login failed")

    #获取本科那个链接，并且点入进入选项卡
    teacher=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="operationSystem"]/div/div/ul/li[1]/a')))
    teacher.click()

    #进入选项卡
    browser.switch_to_window(browser.window_handles[1])
    student=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/table/tbody/tr[4]/td/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/a')))
    student.click()
    table=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/table/tbody/tr[4]/td/table/tbody/tr[3]/td/table/tbody/tr/td[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/a')))
    table.click()
    browser.switch_to_window(browser.window_handles[2])

    #点击各种
    select=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/form/select/option[9]')))
    select.click()
    input=browser.find_element_by_xpath("//input")
    input.send_keys(studentNumber)
    submit=browser.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/form/input[2]')
    submit.click()
    return browser.page_source

def writeme(source):
    file=open("test.txt","w+",encoding="utf-8")
    file.write(source)
    file.close()

source=get_source()
writeme(source=source)
