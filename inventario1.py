import numpy as np
import matplotlib.pyplot as plt
 
P = [[0.9 ,0.075,0.025],
     [0.15,0.8  ,0.05 ],
     [0.25,0.25 ,0.5] ]

S = ['Bull market','Bear market','Stagnant market']

def funcIndicadora(u, bajo, alto):
    if ((u > bajo) & (u <= alto)):
        return 1
    else:
        return 0


def g(u):
    global S, a
    ans = 0
    for i in range(len(S)):
        # print i
        lower, upper = 0, 0
        for k in range(i):
            lower += a[k]
            # print lower
        for k in range(i+1):
            upper += a[k]
        
        temp = funcIndicadora(u,lower, upper)
   
        ans += (i+1)*temp
        # ans += (i+1)*funcIndicadora(u,lower, upper)
    return ans

def f(i,u):
    global P
    ans = 0

    for j in range(len(P)):
        lower, upper = 0,0
        for k in range(j):
            lower += P[i][k]
        for k in range(j+1):
            upper += P[i][k]
        # print 'upper ' + str(upper)
        # print "lower " + str(lower)
        ans += (j+1) * funcIndicadora(u,lower,upper)
    return ans


a = np.random.rand(len(S))
a /= sum(a)

x_0 = g(np.random.rand())
print x_0
xn=x_0
for i in range(100):
    xn = f(xn-1,np.random.rand())
    print xn