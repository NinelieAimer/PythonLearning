#天天向上的力量最终版
def dayUP(df):
	dayup=1
	for i in range(365):
		if i%7 in [0,6]:
			dayup=dayup*(1-0.01)
		else:
			dayup=dayup*(1+df)
		return dayup
dayfactor=0.01
while dayUP(dayfactor)<37.78:
	dayfactor+=0.001
print("工作日应该努力{:2f}".format(dayfactor))
