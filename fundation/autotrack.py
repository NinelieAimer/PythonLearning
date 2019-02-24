#autotrace
import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)

#读取数据
datals=[]
f=open("data.txt")
for line in f:
	line=line.replace("\n","")
	datals.append(list(map(eval,line.split(","))))	#map函数是将第一个参数的功能作用于第二个参数的所有数字，就是对集合中每一个函数执行一次
f.close()
	

#自动绘制
for i in range(len(datals)):
	t.pencolor(datals[i][3],datals[i][4],datals[i][5])
	t.fd(datals[i][0])
	if datals[i][1]:
		t.right(datals[i][2])
	else:
		t.left(datals[i][2])
t.hideturtle()
		
