#绘制蟒蛇
'''
import 保留字
引入了一个绘图库
python计算生态 = 标准库 + 第三方库
turtle(海龟)
RGB通道
255，255，255      1，1，1白色
使用import保留字完成，<a>.<b>()编码风格
import<库名>
<库名>.<函数名>(函数参数)
import<库名>as<库别名>
<库别名>.<函数名>(<函数参数>)
'''

import turtle
turtle.setup(650,350,0,0)  #宽度，高度，起始点x坐标，起始点y坐标，setup并不是必须的
turtle.penup()    #拿起画笔，
turtle.fd(-250)   #运动控制函数forward，海龟走直线
turtle.pendown()    #放下画笔
turtle.pensize(25)  #画笔宽度
turtle.pencolor("purple")   #修改画笔颜色
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)    #
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()


