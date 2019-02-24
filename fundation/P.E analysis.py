from random import random
def printintro():   #提示信息
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")

def getinputs():    #获取输入值
    a=eval(input("请输入选手A的能力值(0-1)"))
    b=eval(input("请输入选手B的能力值(0-1)"))
    n=eval(input("模拟比赛场次："))
    return a,b,n

def printsummary(winsA,winsB): #定义一个输出函数
    n=winsA+winsB
    print("选手A获胜{}场，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场，占比{:0.1%}".format(winsB,winsB/n))

def gameover(a,b):  #定义一个结束函数
    return a==15 or b==15

def simonegame(proA,proB): #模拟一场比赛
    scoreA,scoreB=0,0
    serving="A"
    while not gameover(scoreA,scoreB):
        if serving=="A":
            if random()<proA:
                scoreA+=1
            else:
                serving="B"
        else:
            if random()<proB:
                scoreB+=1
            else:
                serving="A"
    return scoreA,scoreB

def simngames(n,proA,proB):  #模拟n场比赛
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=simonegame(proA,proB)
        if scoreA>scoreB:
            winsA+=1
        else:
            winsB+=1
    return winsA,winsB


def main(): #主要调用函数
    printintro()
    proA,proB,n=getinputs()
    winsA,winsB=simngames(n,proA,proB)
    printsummary(winsA,winsB)

main()