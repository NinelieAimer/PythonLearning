#汉诺塔递归实例
counter=0
def hanoi(n,src,dst,mid): #圆盘数量，源柱子，目标柱子，过度柱子
	global counter
	if n==1:
		print('{}:{}->{}'.format(1,src,dst))
		counter+=1
	else:
		hanoi((n-1),src,mid,dst)
		print('{}:{}->{}'.format(n,src,dst))
		counter+=1
		hanoi(n-1,mid,dst,src)
hanoi(8,"A",'B','C')
