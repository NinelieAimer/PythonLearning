
#数据读取
datals=[]
f=open("data.txt")
for line in f:
	line=line.replace("\n","")
	datals.append(list(map(eval,line.split(","))))	#map函数是将第一个参数的功能作用于第二个参数的所有数字，就是对集合中每一个函数执行一次
f.close()
print(datals)
