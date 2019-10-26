# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 01:50:24 2018

@author: 陈玲倩
"""
#批量读入表格
import os
import pandas as pd
import numpy as np
from glob import glob

P = ('C','D','E','F','G')
for i in P:
    paths = glob(i+':\\**\\Rppp', recursive=True)
    if paths!= []:
        path = ''.join(paths)
        break
    else:
        pass
filename = os.listdir(path+'\\陈·算法')[2:]

#将11张表融合
all = []
for i in range(len(filename)):
    temp = (pd.read_excel(path+'\\陈·算法\\'+filename[i], sheet_name='规格品汇总'))
    temp = temp.iloc[3:, 0:3]
    temp = temp.rename(columns={'Unnamed: 2':filename[i][:-5], 'Unnamed: 1':'规格'})
    all.append(temp) 

data_all = pd.DataFrame(all[0])
for i in range(1,len(all)):
    data_all = pd.concat([data_all,all[i].iloc[:,2]], axis=1)  
    
#修改行名
ID = [x[0:7] for x in data_all.iloc[:,0]]
data_all.iloc[:,0] = ID

#删除0值所在行
idata = data_all.drop(data_all[data_all['南昌'].isin([0])].index.tolist()) 

#删除缺失值所在行
idata = idata.dropna(axis = 0)

#对价格求对数并写入新表
def log_col(city_name):
    idata[city_name] = idata.apply(lambda x:np.log(x[city_name]),axis=1)
for city_name in idata.columns[2:len(filename)+2]:
    log_col(city_name)
idata.head()

co = []
for group in idata.groupby(idata['表2. 各规格品汇总表']):
    b = pd.melt(group[1],id_vars=['规格'],value_vars=['上饶','九江','南昌','吉安','宜春','抚州','新余','景德镇','萍乡','赣州','鹰潭'])#融合数据
    e = pd.get_dummies(b['规格'])#将变量变为哑变量
    e = e.drop(e.columns[0],axis=1)
    f = pd.get_dummies(b['variable'])
    f = f.drop(['南昌'],axis=1)
    x = [e,f]
    x = pd.concat(x,axis=1)
    y = np.array(b.iloc[:,2].values.tolist())
    #回归
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()
    reg.fit(x,y)
    coef = reg.coef_
    #intercept = reg.intercept_
    coef = pd.DataFrame(coef)
    #后十位系数为地区ppp
    rcoef = coef.iloc[-10:,0]
    d = np.exp(rcoef)
    d = d.reset_index(drop=True)
    co.append(d)
co = pd.DataFrame(co)
co['南昌']= tuple(np.repeat(1, [len(co)], axis=0))
co.columns=['上饶','九江','吉安','宜春','抚州','新余','景德镇','萍乡','赣州','鹰潭','南昌']
co.insert(0,'规格',([i for i in range(1,len(co)+1)]))
co.to_excel(path+'CPD法\\小类ppp.xlsx',sheet_name='Sheet1',index = False)
