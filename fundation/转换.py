#温度转换.py
tem=input("请输入一个带有符号的温度值")
if tem[0] in ['C','c']:
	F=1.8*eval(tem[1:])+32
	print("F{:.2f}".format(F))
elif tem[0] in ['F','f']:
	C=(eval(tem[1:])-32)/1.8
	print("C{:.2f}".format(C))
else:
        print("输入格式错误")
