'''
round(x,d) #对x四舍五入，d是小数截取位数
浮点数间运算及比较用round()函数辅助
复数：
#DayDayUp.py
dayup =1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
     dayup*=(1-dayfactor)
    else:
        dayup *=(1+dayfactor)
    print("{:.2f}".format(dayup))
'''

def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup*=(1 - 0.01)
        else:
            dayup*=(1 + df)
        return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日对努力参数是：{:3f}".format(dayfactor))