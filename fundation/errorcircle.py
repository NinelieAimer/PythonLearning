#用错误来退出循环
try:
    while True:
        print(A.pop(),end="")   #如果空的时候会报错
except:
    pass
