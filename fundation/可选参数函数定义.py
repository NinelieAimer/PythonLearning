#实例七段数码管的问题分析
import turtle
def drawline(draw): #绘制单段数码管
	turtle.pendown() if draw else turtle.penup()  #这里的意思是draw是ture的意思
	turtle.fd(40)
	turtle.right(90)
def drawdigit(digit): #判断是否绘制
	drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
	drawline(True) if digit in [0,1,3,4,5,6,7,8,7] else drawline(False)
	drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
	drawline(True) if digit in [0,2,6,8] else drawline(False)
	turtle.left(90)
	drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
	drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
	drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
	turtle.left(180)
	turtle.penup()
	turtle.fd(20)
def drawDate(date):
	for i in date:
		drawdigit(eval(i))
def main():
	turtle.setup(800,350,200,200)
	turtle.penup()
	turtle.fd(-300)
	turtle.pensize(5)
	drawDate("20181010")
	turtle.hideturtle()
	turtle.done()
main()
