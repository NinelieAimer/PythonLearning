a=eval(input("输入一个票面利率"))
b=eval(input("输入一个本金"))
n=eval(input("输入一个年限"))
s=eval(input("输入一个标准价格"))
for i in range(1,20):
    q = 1 / (1 + i / 100)
    if (a*b/(1+i/100))*(1-q)**n/(1-q)+b/(1+i/100)**n==s:
        print(i)
        break

