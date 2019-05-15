'''
自动轨迹绘制
        -需求：根据脚本来绘制图形
        -不是写代码而是写数据绘制轨迹
        -数据脚本是自动化最重要的第一步

基本思路
        -步骤1：定义数据文件格式（接口）
        -步骤2：编写程序，根据文件接口解析参数绘制图形
        -步骤3：编制数据文件
'''

import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))
    #map：对一个列表和一个类型的组合元素都实行一次第一个参数所对应都函数
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])