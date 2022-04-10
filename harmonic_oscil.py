import numpy as np
import matplotlib.pyplot as plt

A  = float(input('Insert amplitude A: '))  #amplitude      [depends tbh]
T = float(input('Insert period T:'))       #period         [s]
phi = float(input('Insert phase φ:'))    #frequency      [rad]
omega = 2*np.pi/T                   #angle frequency[rad/s]
f = 1/T                             #frequency      [s^-1]

t = np.linspace(-10,10,1000)

def wave(t):
    return A*np.cos(omega*t + phi)
plt.plot(t,wave(t))
plt.title(f'Harmonic oscilator with amplitude A={A}, Period T={T}, phase φ={phi}, frequency f={f}')
plt.xlabel('time [s]')
plt.show()