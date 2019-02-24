#函数的定义n!
def jiecheng(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
print(jiecheng(3))
