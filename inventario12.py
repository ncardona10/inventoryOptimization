import numpy as np
import matplotlib.pyplot as plt


N = 500

def iterar(miPromedio,s_min,s_max):
    x = [0]
    xprom = []
    u = [0]
    uprom = []
    for i in range(N):
        # demanda en el n-esimo dia
        # print(i)
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
    # plt.plot(suma)
    miPromedio.append(suma[-1])

def xyu(s_min,s_max):
    prom = []
    for i in range(200):
        
        iterar(prom,s_min,s_max)
    return (np.average(prom))

s_min = 3
s_max = 8

# print(xyu(s_min,s_max))
arch = open("punto12.dat",'w')
arch.write("s_min s_max xyu\n" )
for i in range(0,9):
    for j in range(i+1,9):
        temp = xyu(i,j)
        print("s_min: "+str(i)+  " s_max: "+str(j) + " xyu: " + str(temp) )
        arch.write(str(i)+  " "+str(j) + " " + str(temp) + "\n" )

arch.close()

print("terminado.")

