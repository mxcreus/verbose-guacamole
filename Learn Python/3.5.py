'''

文本进度条


import time
scale = 100
print("-------执行开始--------")
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i/scale)*100
    print("{:.3f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)

print("-------执行结束---------")



文本进度条刷新
刷新本质：用后打印的字符覆盖的字符
不能换行：print()需要被控制
要能回退：打印后光标回退到之前的位置\r
import time
for i in range(101):
    print("\r{:.3f}%".format(i),end="hello") #end，可以不让print换行
    time.sleep(0.1)                     #从而用\r可以回退，也就实现刷新
'''

#
import time
scale = 100
print("Program Start".center(scale//2,"-"))
start = time.perf_counter()    #Timing function，define start time
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start   #duration(the time during which something continues) = currently time - start time
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)
    print("\n"+"Program end".center(scale//2,"-"))


'''
what's more:
    use "perf_counter()"  to count time
    this method is suitable for various calculation problem
    e.g. count the running time for one part of program;compare different algorithm;
    
'''