#简单的天天向上
dayfactor=0.01
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print("向上{:.2f},向下{:.2f}".format(dayup,daydown))
