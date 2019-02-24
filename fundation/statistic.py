#statistic
def getnum():   #获得输入,多次输入获得的方法
	nums=[]
	inumstr=input("请输入数字（回车退出）")
	while inumstr!="":
		nums.append(eval(inumstr))
		inumstr=input("请输入数字（回车退出）")
	return nums

def mean(numbers):    #平均数
	s=0
	for num in numbers:
		s=s+num
	return s/len(numbers)

def dev(numbers,mean): #方差
	sdev=0
	for num in numbers:
		sdev=sdev+(num-mean)**2
	return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):	#中位数
        sorted(numbers)
	size = len(numbers)
	if size%2==0:
		med=(numbers[size//2-1])+number[size//2])/2
	else:
		med=numbers[size//2]
	return med

n=getnum()
m=mean(n)
print("平均数：{},方差{},中位数{}".format(m,dev(n,m),median(n)))
