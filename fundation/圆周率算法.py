import time
import random
darts=1000*1000
hits=0
start=time.perf_counter()
for i in range(1,darts+1):
	x,y=random.random(),random.random()
	dist=pow(x**2+y**2,0.5)
	if dist<=1:
		hits+=1
pi=4*(hits/darts)
print("圆周率是{}".format(pi))
	
