#科赫雪花绘制小包裹



import turtle
def koch(size,n):
    if n == 0:
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
    level = 4
    koch(700,level)
    turtle.right(60)
    koch(1200,level)
    turtle.right(30)
    koch(800,level)
    turtle.hideturtule()
main()