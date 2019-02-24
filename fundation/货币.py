cash=input("请输入一种货币")
if cash[0:3] in ['RMB']:
	D=eval(cash[3:])/6.78
	print("转换后的货币为USD{:.2f}".format(D))
elif cash[0:3] in ['USD']:
	R=eval(cash[3:])*6.78
	print("转换后的货币为RMB{:.2f}".format(R))
else:
	print("输入格式错误")
