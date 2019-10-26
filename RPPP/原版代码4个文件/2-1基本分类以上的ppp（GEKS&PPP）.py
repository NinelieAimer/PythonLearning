# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:03:11 2018

@author: 陈玲倩
"""
#上接1.1基本分类ppp（GEKS法）
#本篇代码目的是求出基本分类以上的ppp（中类ppp以及大类ppp）以及GEKS（中类与大类）
#读入权重表中的中类权重和大类权重两个sheet
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
    
bbb1 = pd.read_excel(path+'\\GEKS法\\小类ppp.xlsx')
####改行名列名#####
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
bbb1['规格']= tuple(np.repeat(x, [29,4,5,5,10,6,12,2,10,1,2,4], axis=0))
bbb1.columns=['大类','上饶','九江','吉安','宜春','抚州','新余','景德镇','萍乡','赣州','鹰潭','南昌']
####下接2.1基本分类以上的ppp（GEKSPP）####
temp_p = bbb1
temp_w = pd.read_excel(path + '\\各地区权重.xlsx', sheet_name = '中类权重')
temp_BigW = pd.read_excel(path + '\\各地区权重.xlsx', sheet_name = '大类权重')
#将价格和权重按大类那列进行分组，并存入数组
p_gro = temp_p.groupby(temp_p['大类'])
w_pro = temp_w.groupby(temp_w['大类'])
p = []
w = []
for i,j in zip(p_gro, w_pro):
    e, g = i
    t, k = j
    p.append(g.values.tolist())
    w.append(k.values.tolist())
#计算中类ppp和中类GEKS
#中类ppp输出结果为12个11*11的表，并且对角线为1，中类GEKS为12*11的表格
#输出结果存入中类ppp的文件夹中
gge = []
#最外一层循环是算12个大类的GEKS
for m in range(len(p_gro)):
    temp_p = np.array(p[m])
    temp_w = np.array(w[m])
    temp_pw = temp_p[:,1:] * temp_w[:,1:]
    sum_pw = np.sum(temp_pw,axis = 0)
    ppp = []
    gg = []
    #这两层循环是算一个大类下，所求城市相对于剩下10个城市的费雪理想双边价格指数
    for n in range(len(p_gro)-1):
        priceaa = []
        for a in range(len(p_gro)-1):
            temp_fm1 = temp_p[:,n+1] * temp_w[:,a+1]
            temp_sum = np.sum(temp_fm1)
            temp_fz1 = temp_w[:,n+1] * temp_p[:,a+1]
            temp_sum2 = np.sum(temp_fz1)
            city_fz = sum_pw[a]
            city_fm2 = sum_pw[n]
            citya = pow(city_fz / temp_sum, 1/2)
            cityb = pow(temp_sum2 / city_fm2, 1/2)
            pricea = citya * cityb
            priceaa.append(pricea)
        #计算geks
        geks = pow(np.prod(priceaa),1/(len(p_gro)-1))
        gg.append(geks)
        #将每次循环输出的ppp合并
        ppp.append(priceaa)
    gge.append(gg)
    ggee = np.array(gge)
    ggee = pd.DataFrame(ggee)
    pppm = np.array(ppp)
    pppm = pd.DataFrame(pppm)
    pppm.insert(0,'地区',(['上饶','九江','吉安','宜春','抚州','新余','景德镇','萍乡','赣州','鹰潭','南昌']))
    pppm.columns=['地区','上饶','九江','吉安','宜春','抚州','新余','景德镇','萍乡','赣州','鹰潭','南昌']
    #将结果ppp和geks存入表格并输出
    pppm.to_excel(path+'\\GEKS法\\中类\\第'+str(m+1)+'个中类ppp.xlsx',sheet_name='Sheet 1',index = False)
ggee.columns=['上饶','九江','吉安','宜春','抚州','新余','景德镇','萍乡','赣州','鹰潭','南昌']
ggee.insert(0,'大类分类',([i for i in range(1,(len(p_gro)+1))]))
ggee.to_excel(path+'\\GEKS法\\中类\\'+'中类GEKS.xlsx',sheet_name='Sheet 1',index = False)
    
#计算大类（方法同中类）
temp = temp_BigW.drop(['分类'], axis = 1)
Big_w = np.array(temp)
Big_p = np.array(ggee.iloc[:,1:])
Big_pw = Big_p * Big_w
sum_Big_pw = np.sum(Big_pw, axis = 0)
bigppp = []
geksgg = []
for b in range(len(Big_p)-1):
    big = []
    for c in range(len(Big_p)-1):  
        fz1 = sum_Big_pw[c]
        fm2 = sum_Big_pw[b]
        fm1f = Big_p[:,b] * Big_w[:,c]
        fm1 = np.sum(fm1f)
        fz2f = Big_p[:,c] * Big_w[:,b]
        fz2 = np.sum(fz2f)
        big_city1 = pow(fz1 / fm1, 1/2)
        big_city2 = pow(fz2 / fm2, 1/2)
        big_city = big_city1 * big_city2
        big.append(big_city)
    geksb = pow(np.prod(big),1/(len(Big_p)-1))
    geksgg.append(geksb)
    GEKS = np.array(geksgg)
    GEKS = pd.DataFrame(GEKS)
    bigppp.append(big)    
    bppp = np.array(bigppp) 
    bppp = pd.DataFrame(bppp)
bppp.insert(0,'地区',(['上饶','九江','吉安','宜春','抚州','新余','景德镇','萍乡','赣州','鹰潭','南昌']))
bppp.columns=['地区','上饶','九江','吉安','宜春','抚州','新余','景德镇','萍乡','赣州','鹰潭','南昌']
GEKS.index = ['上饶','九江','吉安','宜春','抚州','新余','景德镇','萍乡','赣州','鹰潭','南昌']
GEKS.columns = ['大类GEKS']
bppp.to_excel(path+'\\GEKS法\\大类\\大类ppp.xlsx',sheet_name='Sheet 1',index = False)
GEKS.to_excel(path+'\\GEKS法\\大类\\大类GEKS.xlsx',sheet_name='Sheet 1')