# -*- coding: utf-8 -*-
"""SUBPLOT DE OTRAS FORMAS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1olnVx0OD_T_FtDD-0f83OPkIcD3HDWPT
"""

import numpy as np
from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt
from scipy import signal

plt.style.use("seaborn-poster")

fig, ax = plt.subplots(2,2)
fig.tight_layout(pad = 5.5)
fig.subplots_adjust(bottom=0.1,right=1.2,top=1.2)

t1 = np.linspace(0, 1, 500)



#subplots
ax[0,0].plot(t1, signal.sawtooth(20 * np.pi * 2 * t1),color='tab:orange')     #Shawtooh variacion en A y t
ax[0,0].set_title('Signal Sawtooth')

F = 2;
t= np.linspace(-1,1,2*500, endpoint = False)
i, q, e = signal.gausspulse(t, F, retquad=True, retenv=True)
ax[0,1].plot(t,i,t,q,t,e,'--')                                                #Gauseana - en F
ax[0,1].set_title('Signal Gausspulse')


ax[1,1].plot(t1, signal.square(25 * np.pi * 2 * t1),color='tab:purple')       #Square
ax[1,1].set_title('Square wave: s(t) = square (2πft)')


t2 = np.linspace(0,10,1000)
F = 0.5
F1 = 3;
w = chirp(t, f0=6, f1=25, t1=7, method='linear')
ax[1,0].plot(t2,w, color='c')                                                  #Chirp
ax[1,0].set_title(' ')


for i in range(0,2):
  for j in range(0,2):
    ax[i,j].set_ylabel("Amplitud(dBm)")
    ax[i,j].set_xlabel("Time (s)")
    ax[i,j].axhline(y=0,color='k')