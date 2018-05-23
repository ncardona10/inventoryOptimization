import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import binom

mpl.style.use('classic')

bn = binom(10, 0.4)



mpl.rcParams.update({'font.size': 18})


s_min = 3
s_max = 8

N = 500
data = []
def iterar():
    x = [0]
    
    for i in range(N):
        # demanda en el n-esimo dia
        d_n = np.random.binomial(10, 0.4)
        if(x[-1] > s_min & x[-1] <= s_max):
            x.append(max(0, x[-1]-d_n))
        else:
            x.append(max(0, s_max-d_n))
    
    data.append(x[-1])


for i in range(500):
    iterar()

data = np.array(data)

d = np.diff(np.unique(data)).min()
left_of_first_bin = data.min() - float(d)/2
right_of_last_bin = data.max() + float(d)/2
plt.hist(data, np.arange(left_of_first_bin, right_of_last_bin + d, d),normed = True,ec='black')
plt.xlim(-2,11)
plt.xlabel(r"$s$")
plt.ylabel(r"$Frecuencia\ normalizada$")
plt.savefig("histograma.png")
plt.close()



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


P1 = P.copy()

for i in range(499):
    P = np.matmul(P,P1)

print(P)
