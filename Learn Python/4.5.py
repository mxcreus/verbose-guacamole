'''pi
pi = 0
N = 100
for k in range(N):
    pi += 1/pow(16,k)*(\
        4/(8*k+1)-2/(8*k+4)- \
    1/(8*k+5) - 1/(8*k+6))
print(pi)
'''

#Monte Carlo method to calculate pi
from random import random
from time import perf_counter
DARTS = 100000*100000
hits = 0.0
start = perf_counter()  #start timing
for i in range(1,DARTS +1):
    x,y = random(),random()
    dist = pow(x**2+y**2,0.5)
    if dist <= 1.0:
        hits +=1
pi = 4 *(hits/DARTS)
print(pi)
print("{:.3f}".format(perf_counter()-start))
