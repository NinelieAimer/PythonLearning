#函数递归实例解析，字符串反转
def rvs(s):
	if s=='':
		return s
	else:
		return rvs(s[1:])+s[0]
