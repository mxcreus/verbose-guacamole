

TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['f','F']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("{:.2f}C".format(C))
elif TempStr[-1] in ['c','C']:
    F = 1.8*(eval(TempStr[0:-1])) + 32
    print("{:.2f}F".format(F))
else:
    print("format error")
'''
eval("1")
1
评估函数

'''