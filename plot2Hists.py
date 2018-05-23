import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import binom

mpl.style.use('classic')

bn = binom(10, 0.4)


# mpl.rcParams.update({'font.size': 18})


s_min = 3
s_max = 8

N = 500
data = []
proms = []

def iterar():
    x = [0]
    u = [0]
    xprom = []
    uprom =[]
    for i in range(N):
        # demanda en el n-esimo dia
        d_n = np.random.binomial(10, 0.4)
        if(x[-1] > s_min & x[-1] <= s_max):
            u.append(max(0,d_n-x[-1]))
            x.append(max(0, x[-1]-d_n))
        else:
            x.append(max(0, s_max-d_n))
            u.append(max(d_n-s_max,0))
    for i in range(N):
        sum = 0
        sumU = 0 
        for j in range(i):
            sum += x[j]
            sumU += u[j]
        xprom.append((sum+0.0)/(i+1))
        uprom.append((sumU+0.0)/(2*(i+1)))

    data.append(xprom[-1])
    proms.append(xprom[-1]+uprom[-1])


for i in range(500):
    iterar()

fig = plt.figure()
ax = plt.subplot(111)

data = np.array(data)

d = np.diff(np.unique(data)).min()
left_of_first_bin = data.min() - float(d)/2
# right_of_last_bin = data.max() + float(d)/2
ax.hist(data, 
         normed=False, ec='black', alpha=0.5, label = r"$\frac{1}{N}\sum^N_{n=1}X_n$")
ax.hist(proms, 
         normed=False, ec='black', alpha=0.5, label = r"$\frac{1}{N}\sum^N_{n=1}X_n + \frac{1}{2N}\sum^N_{n=1}U_n$")


box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# plt.xlim(-2, 11)
plt.xlabel(r"$s$")
plt.ylabel(r"$Frecuencia\ normalizada$")
# plt.legend(loc = 4)
plt.savefig("ambosHistogramas.png")


plt.close()
