import matplotlib.pyplot as plt
import numpy as np
k = 8 #Hookes constant [N/m]
m = 2 #Mass [kg]
phi = np.arctan(1/0.4)
A = 0.4/np.cos(phi)



t = np.linspace(0,10,1000)
def x(t):
    return A*np.cos(np.sqrt(k/m)*t + phi)

def v(t):
    return -A*np.sqrt(k/m)*np.sin(np.sqrt(k/m)*t + phi)

def p(t):
    return v(t)*m
plt.figure(figsize=(5,4))
plt.plot(x(t),p(t))
plt.xlabel("avstand fra likevektspunkt [m]")
plt.ylabel('bevegelsesmengde [kgm/s]')
plt.savefig('2d_fig.png')
#plt.show()
