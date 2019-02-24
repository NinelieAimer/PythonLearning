i=1
while i<4:
	name=input("请输入用户名")[6:]
	password=input("请输入密码")[5:]
	if name =="Kate" and password=="666666":
		print("登录成功")
		break
	else:
		i=i+1
		if i==4:
			print("3次都错误,退出程序")