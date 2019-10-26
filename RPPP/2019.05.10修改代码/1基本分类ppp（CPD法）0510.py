# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 01:50:24 2018

@author: 陈玲倩
"""
#批量读入表格
import os
import pandas as pd
import numpy as np
import re
#选择存放输入数据文件夹的文件夹(本文中例子为RPPP文件夹)
#这里加对话框
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()
#######
filename = os.listdir(path+'\\输入的数据')
#暂时过滤各地区权重表（命名仅需包含权重两字）
str_convert =','.join(filename)
pattern = re.compile(r'\w*权重\w*',flags=0)
weight = re.findall(pattern,str_convert)
weight = ''.join(weight+['.xlsx'])
filename.remove(weight)

#将各地区数据表融合（示例中为11张表）
all = []
for i in range(len(filename)):
    temp = (pd.read_excel(path+'\\输入的数据\\'+filename[i], sheet_name='规格品汇总'))
    temp = temp.iloc[3:, 0:3]
    temp = temp.rename(columns={'Unnamed: 2':filename[i][:-5], 'Unnamed: 1':'规格'})
    all.append(temp) 

data_all = pd.DataFrame(all[0])
for i in range(1,len(all)):
    data_all = pd.concat([data_all,all[i].iloc[:,2]], axis=1)  
    
#修改行名
ID = [x[0:7] for x in data_all.iloc[:,0]]
data_all.iloc[:,0] = ID

#将0值替换为缺失值
data_all = data_all.replace(0,np.nan)
#删除缺失值所在行
idata = data_all.dropna(axis = 0)

#对价格求对数并写入新表
def log_col(city_name):
    idata[city_name] = idata.apply(lambda x:np.log(x[city_name]),axis=1)
for city_name in idata.columns[2:]:
    log_col(city_name)
idata.head()

#输入基准城市
####也可以加对话框
bas_ppp = []
base_city = '南昌'
#进行哑变量回归
for group in idata.groupby(idata.iloc[:,0]):
    b = pd.melt(group[1],id_vars=[idata.columns[1]],value_vars = [x for x in idata.columns[2:]])#融合数据
    e = pd.get_dummies(b[idata.columns[1]])#将变量变为哑变量
    e = e.drop(e.columns[0],axis=1)
    f = pd.get_dummies(b.iloc[:,1])
    f = f.drop([base_city],axis=1)
    x = [e,f]
    x = pd.concat(x,axis=1)
    y = np.array(b.iloc[:,2].values.tolist())
    #回归
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()
    reg.fit(x,y)
    coef = reg.coef_
    coef = pd.DataFrame(coef)
    #后几位系数为地区ppp（此示例数据中为后十位）
    rcoef = coef.iloc[-(len(idata.columns)-3):,0]
    d = np.exp(rcoef)
    d = d.reset_index(drop=True)
    bas_ppp.append(d)
bas_ppp = pd.DataFrame(bas_ppp)
bas_ppp[base_city]= tuple(np.repeat(1, [len(bas_ppp)], axis=0))
bas_ppp.columns = [x for x in f.columns]+[base_city]
#创建输出结果文件夹
path2 = path+'\\输出的结果\\'
os.makedirs(path2)
bas_ppp.to_excel(path2+'\\基本分类ppp.xlsx',sheet_name='Sheet1',index = False)

