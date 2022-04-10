#modules
import numpy as np
import matplotlib.pyplot as plt


f1 = 261.64 #Hz
f2 = 277.18 #Hz

#constnants
L = 30e-3   #length bassilarmembrane, meter
N = 3000    #amount of nervecells
dl = L/N
F=1 #Nm
#arrays
width = np.linspace(0.1e-3,0.3e-3,N)
thickness = np.linspace(0.3e-3,0.1e-3,N) 
rho = np.linspace(1500,2500,N)
x = np.linspace(0,L,N)
k_log = np.logspace(-6,-1,N)
k_lin = np.linspace(10**-6,10**-1,N)
mass = width*thickness*rho*dl

omega_0_lin = np.sqrt(k_lin/mass)



def A(b,f):
    omega_F =  f*2*np.pi
    return F/mass/np.sqrt((omega_0_lin**2 - omega_F**2)**2 + (b*omega_F/mass)**2)

"""for i in range(0,10):
    b = 1*10**-i
    plt.plot(x,A(b,f1),label=f'{f1}Hz')
    plt.plot(x,A(b,f2),label=f'{f2}Hz')
    plt.xlabel('x [m]')
    plt.ylabel('Amplitude [m]')
    plt.legend()
    plt.title(f'b = {b}')
    plt.show()"""


A1 = A(1*10**-8,f1)
A2 = A(1*10**-8,f2)

max1 = np.max(A1)
index_max1 = np.where(max1==A1)[0][0]
print('Q factor=',mass[index_max1]*omega_0_lin[index_max1]/(1*10**-8))

print('delta t = ',mass[index_max1]*omega_0_lin[index_max1]/(1*10**-8)/omega_0_lin[index_max1])