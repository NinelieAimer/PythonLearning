#BMI最终版
height,weight=eval(input("青输入身高和体重"))
bmi=weight/pow(height,2)
who,nat="",""
if bmi<18.5:
	who,nat="偏瘦","偏瘦"
elif 18.5<=bmi<=24:
	who,nat="正常","正常"
elif 24<=bmi<=25:
	who,nat="偏胖","偏瘦"
elif 25<=bmi<=28:
	who,nat="偏胖","偏瘦"
elif 28<=bmi<=30:
	who,nat="肥胖","肥胖"
else:
	who,nat="肥胖","肥胖"
print("BNI指标为国内{},国际{}".format(who,nat))
