#modules
import numpy as np
import matplotlib.pyplot as plt

#constnants
L = 30e-3   #length bassilarmembrane, meter
N = 3000    #amount of nervecells
dl = L/N
#arrays
width = np.linspace(0.1e-3,0.3e-3,N)
thickness = np.linspace(0.3e-3,0.1e-3,N) 
rho = np.linspace(1500,2500,N)
x = np.linspace(0,L,N)
k_log = np.logspace(-6,-1,N)
k_lin = np.linspace(10**-6,10**-1,N)
mass = width*thickness*rho*dl
print(mass)

f_log = np.sqrt(k_log/mass)/(2*np.pi)
f_lin = np.sqrt(k_lin/mass)/(2*np.pi)

plt.plot(x,f_log,label='f_log')
plt.plot(x,f_lin,label='f_lin')
plt.xlabel('x [m]')
plt.ylabel('frequency [Hz] ')
plt.legend()
plt.show()

