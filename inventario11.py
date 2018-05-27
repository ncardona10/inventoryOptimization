import numpy as np
import matplotlib.pyplot as plt

s_min = 3
s_max = 8

N = 500

def iterar():
    x = [0]
    xprom = []
    u = [0]
    uprom = []
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

    suma = np.array(xprom)+np.array(uprom)
    print("xprom " + str(xprom[-1]))
    print("uprom " + str(uprom[-1]))
    print("suma " + str([-1]))
    plt.plot(suma)
    # plt.plot(xprom,c="blue")
    # plt.plot(uprom,c="black")


for i in range(100):
    iterar()



plt.grid(True,linestyle='--')
plt.xlabel(r"$N$")
plt.ylabel(r"$\frac{1}{N} \sum^N_{n=1} X_n  + \frac{1}{2N} \sum^N_{n=1}U_n$")
# plt.title(r"$Punto\ 9$")
plt.ylim(0,4)
plt.xlim(0,500)
plt.legend()
plt.savefig("punto11.png")
plt.close()
