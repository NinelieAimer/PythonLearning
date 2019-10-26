# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:05:43 2018

@author: 陈玲倩
"""
#本篇代码作用与命名为GEKS&PPP的代码相同，都求出了GEKS，但是并未输出ppp
#因为循环方式不同，但是最终求出的GEKS（中类&大类GEKS）相同，在另一层面上验证了结果的可靠性
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

temp_p = pd.read_excel(path+'\\CPD法\\小类ppp.xlsx')
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
temp_p['规格']= tuple(np.repeat(x, [29,4,5,5,10,6,12,2,10,1,2,4], axis=0))
temp_p.columns=['大类','上饶','九江','吉安','宜春','抚州','新余','景德镇','萍乡','赣州','鹰潭','南昌']
#读入权重表中的中类权重和大类权重两个sheet
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
#计算中类
#拉氏（开根后）
pw = []
for m in range(len(p_gro)):
    cat = []
    temp_p = np.array(p[m])
    temp_w = np.array(w[m])
    temp_pw = temp_p[:,1:]  * temp_w[:,1:] 
    sum_pw = np.sum(temp_pw,axis = 0)
    
    for n in range(len(p_gro)-1):
        city_fz = np.prod(sum_pw)
        temp_fm = []
        for a in range(len(p_gro)-1):
            temp_fm1 = temp_p[:,n+1] * temp_w[:,a+1]
            temp_sum = np.sum(temp_fm1)
            temp_fm.append(temp_sum)
        
        city_fm = np.prod(temp_fm)
        city = pow(city_fz / city_fm, 1/((len(p_gro)-1)*2))
        cat.append(city)
    pw.append(cat)
cat_p = np.array(pw)

#帕氏（开根后）
pw2 = []
for b in range(len(p_gro)):
    cat2 = []
    temp_p2 = np.array(p[b])
    temp_w2 = np.array(w[b])
    temp_pw2 = temp_p2[:,1:]  * temp_w2[:,1:] 
    sum_pw2 = np.sum(temp_pw2,axis = 0)
    
    for c in range(len(p_gro)-1):
        city_fm2 = pow(sum_pw2[c],(len(p_gro)-1))
        temp_fz2 = []
        for d in range((len(p_gro)-1)):
            temp_fz1 = temp_w2[:,c+1] * temp_p2[:,d+1]
            temp_sum2 = np.sum(temp_fz1)
            temp_fz2.append(temp_sum2)
        
        city_fz2 = np.prod(temp_fz2)
        city2 = pow(city_fz2 / city_fm2, 1/((len(p_gro)-1)*2))
        cat2.append(city2)
    pw2.append(cat2)
cat2_p = np.array(pw2)

#拉氏指数*帕氏指数（开根后），即为中类的GEKS
cat3_p = cat_p * cat2_p

#相同方法计算大类
temp = temp_BigW.drop(['分类'], axis = 1)
Big_w = np.array(temp)
big_pw = cat3_p * Big_w
sum_big_pw = np.sum(big_pw, axis = 0)

#拉式（开根后）
big_p = []
for i in range((len(p_gro)-1)):  
    big_city_fz = np.prod(sum_big_pw)
    temp_bigfm = []
    for c in range((len(p_gro)-1)):
        temp_bigfm1 = cat3_p[:,i] * Big_w[:,c]
        temp_bigsum = np.sum(temp_bigfm1)
        temp_bigfm.append(temp_bigsum)
        
    big_city_fm = np.prod(temp_bigfm)
    big_city = pow(big_city_fz / big_city_fm, 1/((len(p_gro)-1)*2))
    big_p.append(big_city)
big_p = np.array(big_p)

#帕氏（开根后）
big_p2 = []
for e in range((len(p_gro)-1)):
    big_city_fm2 = pow(sum_big_pw[e],(len(p_gro)-1))
    temp_bigfz = []
    for f in range(11):
        temp_bigfz1 = Big_w[:,e] * cat3_p[:,f]
        temp_bigsum2 = np.sum(temp_bigfz1)
        temp_bigfz.append(temp_bigsum2)
    
    big_city_fz2 = np.prod(temp_bigfz)
    big_city2 = pow(big_city_fz2 / big_city_fm2, 1/((len(p_gro)-1)*2))
    big_p2.append(big_city2)
big_p2 = np.array(big_p2)  

#拉氏指数*帕氏指数（开根后）
big_ppp = big_p * big_p2   
       
result = pd.DataFrame(np.array(big_ppp).reshape(1,-1))
result.columns = ['上饶','九江','吉安','宜春','抚州','新余','景德镇','萍乡','赣州','鹰潭','南昌']
result.to_excel(path + '\\CPD法\\大类GEKS.xlsx',index = False)
