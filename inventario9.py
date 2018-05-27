import numpy as np
import matplotlib.pyplot as plt

s_min = 3
s_max = 8

N = 500


def iterar():
    x = [0]
    xprom = []
    for i in range(N):
        # demanda en el n-esimo dia
        d_n = np.random.binomial(10, 0.4)
        if(x[-1] > s_min & x[-1] <= s_max):
            x.append(max(0, x[-1]-d_n))
        else:
            x.append(max(0, s_max-d_n))

    for i in range(N):
        sum = 0
        for j in range(i):
            sum += x[j]
        xprom.append((sum+0.0)/(i+1))

    plt.plot(xprom)


for i in range(100):
    iterar()



plt.grid(True,linestyle='--')
plt.xlabel(r"$N$")
plt.ylabel(r"$\frac{1}{N} \sum^N_{n=1} X_n $")
# plt.title(r"$Punto\ 9$")
ys = np.zeros(500) + 2.8830663307574635
plt.plot(ys,lw = 2,c = "black",label = r"$\pi (f) := \sum_{i\in S}f(i)\pi_i = 2.88$")
plt.xlim(0,500)
plt.ylim(0,4)
plt.legend()
plt.savefig("punto9.png")
plt.close()
