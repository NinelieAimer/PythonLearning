#可变参数练习函数
def fact(n,*b):
    s=1
    for i in range(1,n+1):
        s*=i
    for item in b:
        s*=item
    return s
print(fact(10,3))
