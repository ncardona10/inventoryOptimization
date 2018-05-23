import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from numpy import linalg as LA

s_min = 3
s_max = 8
bn = binom(10, 0.4)

P = np.zeros((9, 9))

for i in range(4):
    P[i][0] = 1-bn.cdf(7)
for i in range(1, 9):
    for j in range(4):
        P[j][i] = bn.pmf(8-i)

for i in range(4, 9):
    P[i][0] = 1-bn.cdf(i-1)
for i in range(4, 9):
    for j in range(1, i+1):
        P[i][j] = bn.pmf(i-j)

w, v  = LA.eig(np.transpose(P))
np.set_printoptions(precision=3)

eigv = v[:,0].real/sum(v[:,0].real)
plt.plot(eigv)
plt.xlabel(r"$s$")
plt.ylabel(r"$\pi(s)$")
plt.grid(True,linestyle = '--')
plt.savefig("pi.png")

sum = 0 
for i in range(9):
    sum += i*eigv[i]
print(sum)
