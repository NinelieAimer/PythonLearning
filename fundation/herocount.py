#countword2
import jieba
txt=open("threekingdoms.txt",'r',encoding='utf-8').read()
aph=jieba.lcut(txt)  #得到列表

counts={}	#定义一个空字典
for a in aph:
	if len(a)==1:
		continue
	else:
		counts[a]=counts.get(a,0)+1
item=list(counts.items())
item.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
	a,number=item[i]
	print("{0:<10}{1:>5}".format(a,number))		
