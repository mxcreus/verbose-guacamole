#七段数码管
'''
步骤
绘制单个数字对应数码管
获得一串数字，绘制对应数码管
获得当前系统时间，绘制对应数码管
'''

import turtle
import  time
def drawGap():
    turtle.penup()
    turtle.fd(20)
def drawline(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(100)
    drawGap()
    turtle.right(90)
def drawdigit(digit):
     drawline(True) if digit in [2,3,5,6,8,9] else drawline(False)
     drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
     drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
     drawline(True) if digit in [0,2,6,8] else drawline(False)
     turtle.left(90)
     drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
     drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
     drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
     turtle.left(180)
     turtle.penup()
     turtle.fd(30)
def drawdate(date):
    turtle.pencolor("red")
    for i in date:
        if i == "-":
            turtle.write("年",font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == "=":
            turtle.write("月", font=("Arial", 18, "normal"))
        elif i == "+":
            turtle.write("日",font=("Arial",18,"normal"))
        else:
            drawdigit(eval(i))

def main():
        turtle.setup(800,350,200,200)
        turtle.penup()
        turtle.fd(-300)
        turtle.pensize(5)
        drawdate(time.strftime("%Y-%m=%d+",time.gmtime()))
        turtle.hideturtle()
        turtle.done
main()

'''
模块化思维：确定模块接口，封装功能
规则化思维：抽象过程为规则，计算机自动执行
化繁为简：将大功能变为小功能组合，分而治之


'''