'''函数和对象是代码复用的两种主要形式
函数：将代码命名 在代码层面建立了初步抽象
对象：属性和方法
紧耦合：两个部分之间交流很多，无法独立存在
松耦合：两个部分之间交流较少，可以独立存在


递归的定义：
链条：计算过程存在递归链条
基例：存在一个或多个不需要再次递归的基例
类似数学归纳法

a = eval(input())

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
print(fact(a))

#递归字符串反转
def reserve(s):
    if s == "":
        return s
    else:
        return reserve(s[1:])+s[0]
'''

#hanoi
count = 0
n = eval(input())
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count +=1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}_>{}".format(n,src,dst))
        count +=1
        hanoi(n-1,mid,dst,src)
print(hanoi(n,"A","C","B"))
print(count)