# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:47:45 2018

@author: 陈玲倩
"""
#本篇代码与CPD法的作用一致 都求出了基本分类ppp
#结果相同，验证了结果的可靠性
#批量读入表格
import os
import pandas as pd
import numpy as np
import re
#选择存放输入数据文件夹的文件夹(本文中例子为RPPP文件夹)

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()
#全局搜索代码
#from glob import glob
#
#P = ('C','D','E','F','G')
#for i in P:
#    paths = glob(i+':\\**\\Rppp', recursive=True)
#    if paths!= []:
#        path = ''.join(paths)
#        break
#    else:
#        pass
#path = 'C:\\Users\\Administrator\\Desktop\\Rppp\\'##文件夹存放的路径
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

#以南昌为基准，算各个区域的相对价格
column = list(idata.columns)

for i in range(column.index('规格')+1,column.index('南昌')):
    idata[i]=idata.apply(lambda x:x[i]/x[column.index('南昌')],axis=1)
for j in range(column.index('南昌')+1,len(filename)+2):  
    idata[j]=idata.apply(lambda x:x[j]/x[column.index('南昌')],axis=1)
idata[13]=idata.apply(lambda x:x[column.index('南昌')]/x[column.index('南昌')],axis=1)
idata = idata.rename(columns={2:'上饶1',3:'九江1',5:'吉安1',6:'宜春1',7:'抚州1',8:'新余1',9:'景德镇1',10:'萍乡1',11:'赣州1',12:'鹰潭1',13:'南昌1'
})
    
#定义计算几何平均数函数
def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod()**(1.0/len(a))

#计算不同分类，不同地区的几何平均
group = idata.iloc[:,13:].groupby(idata['表2. 各规格品汇总表'])

bbb = []
for g,h in group:
    aaa = []
    aaa.append(g)
    for j in h:
        gm = geo_mean(h[j].values)
        aaa.append(gm) 
        #print(g,gm)
    aaa = np.array(aaa).reshape(-1,12)
    df = pd.DataFrame(aaa)
    df.columns = list(idata.columns)[12:24]
    df = df.rename(columns = {'鹰潭' : '规格'})
    bbb.append(df)
bbb1 = pd.concat(bbb,axis = 0)
bbb1.to_excel(path+'\\GEKS法小类ppp.xlsx',index=False)  

