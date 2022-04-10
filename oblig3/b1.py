"""Modules"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
"""Parameters"""
#below are given specifically in assignment
f = 800 #Hz, Frequency
f_s = 1e3 #Hz, sample frequency
A = 1 #m, ????
T = 1 #s, sample period.
dt = 1/f_s #timestep, s
N = int(T/dt)

t = np.arange(0,T,dt) #time array from 0 to T, with increment dt.


def g(t):
    return A*np.sin(2*np.pi*f*t)

x = A*np.sin(2*np.pi*f*t)

"""plt.plot(t,g(t))
plt.xlabel('t [s]')
plt.ylabel('No clue, [m]')
plt.show()"""


x_fourier = fft.fft(x)
f_array = fft.fftfreq(N,dt)
plt.title('f=800Hz')
plt.bar(f_array,np.abs(x_fourier))
plt.xlabel('Frequency [Hz]')
plt.ylabel('unsure')
plt.show()