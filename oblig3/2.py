"""Modules"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
"""Constants"""
A1 = 1      #m
A2 = 1.7    #m
f1 = 100    #Hz, frequency 1
f2 = 160    #Hz, frequency 2
t1 = 0.2    #s
t2 = 0.6    #s
sigma1 = 0.05   #s
sigma2 = 0.10   #s

f_s = 1e3       #Hz
T = 1           #s
dt = 1/f_s #timestep, s
N = int(np.ceil(T/dt))


def f(t):
    A = A1*np.sin(2*np.pi*f1*t)*np.exp((t-t1/sigma1)**2)
    B = A2*np.sin(2*np.pi*f2*t)*np.exp((t-t2/sigma2)**2)
    return A+B

t = np.arange(0,T,dt) #time array from 0 to T, with increment dt.
x = f(t)


plt.plot(t,x)
plt.xlabel('t [s]')
plt.ylabel('No clue, [m]')
plt.show()

x_fourier = fft.fft(x)
f_array = fft.fftfreq(N,dt)

plt.bar(f_array,np.abs(x_fourier))
plt.xlabel('Frequency [Hz]')
plt.ylabel('unsure')
plt.show()
