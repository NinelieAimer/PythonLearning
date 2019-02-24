#kochdraw2
import turtle
def koch(size,n):
	if n==0:
		turtle.fd(size)
	else:
		for angle in [0,60,-120,60]:
			turtle.left(angle)
			koch(size/3,n-1)
def main():
	turtle.setup(600,600)
	turtle.penup()
	turtle.goto(-200,100)
	turtle.pendown()
	turtle.pensize(2)
	level=eval(input("输入应该想要的阶数"))
	for i in range(level):
		koch(400,level)
		turtle.right(360/level)
	turtle.hideturtle()
main()
