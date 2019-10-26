# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:03:11 2018

@author: 陈玲倩
"""
#上接1基本分类ppp（CPD法）
#本篇代码目的是求出基本分类以上的ppp以及GEKS 
import pandas as pd
import numpy as np
import os
import re
#选择存放输入数据文件夹的文件夹(本文中例子为RPPP文件夹)
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()

#path = 'C:\\Users\\Administrator\\Desktop\\Rppp\\'##文件夹存放的路径
bas_ppp = pd.read_excel(path+'\\输出的结果\\基本分类ppp.xlsx','Sheet1')
#查找输入的数据文件夹中的权重表（命名仅需包含权重两字）
filename = os.listdir(path+'\\输入的数据')
str_convert =','.join(filename)
pattern = re.compile(r'\w*权重\w*',flags=0)
weight = re.findall(pattern,str_convert)
weight = ''.join(weight+['.xlsx'])
#读入权重表
temp_w = pd.read_excel(path + '\\输入的数据\\'+weight)
#最终ppp输出结果为11*11的表，并且对角线为1，GEKS为1*11的表格
ppp = []
geks = [] 
temp_p = np.array(bas_ppp)
temp_w = np.array(temp_w)
#这两层循环是基准地区相对于剩下几个地区的费雪理想双边价格指数
for j in range(len(bas_ppp.columns)):
    price = []     
    for k in range(len(bas_ppp.columns)):
        pjqj = np.sum(temp_p[:,j] * temp_w[:,j])
        pkqj = np.sum(temp_p[:,k] * temp_w[:,j])
        p_l = pjqj/pkqj
        pjqk = np.sum(temp_p[:,j] * temp_w[:,k])
        pkqk = np.sum(temp_p[:,k] * temp_w[:,k])
        p_p = pjqk/pkqk
        pricec = pow(p_l*p_p,1/2)     
        price.append(pricec)
    #计算geks
    geksc = pow(np.prod(price),1/len(bas_ppp.columns))
    geks.append(geksc)
    #将每次循环输出的ppp合并
    ppp.append(price)
geks = np.array(geks)
geks = pd.DataFrame(geks)
ppp = np.array(ppp)
ppp = pd.DataFrame(ppp)
ppp.insert(0,'地区',([x for x in bas_ppp.columns]))
ppp.columns=['地区']+[x for x in bas_ppp.columns]   #bas_ppp.tolist()
#将结果ppp和geks存入表格并输出
ppp.to_excel(path+'\\输出的结果\\最终ppp.xlsx',sheet_name='Sheet 1',index = False)
geks = geks.T
geks.columns=[x for x in bas_ppp.columns]
geks.insert(0,'地区',('GEKS'))
geks.to_excel(path+'\\输出的结果\\GEKS.xlsx',sheet_name='Sheet 1',index = False)