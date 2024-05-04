# -*- coding: utf-8 -*-
"""FUNCIÓN SINOSUIDAL

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18PNPGW9pTEkKt9jmbAtVPd-qTJOnsfVJ
"""

import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-poster")

x= np.linspace(0,100, 800)# incremento del 0.1
y = np.sin(x)

plt.Figure(figsize=(8,6))
plt.plot(x,y,"g")
plt.xlabel("Time")
plt.ylabel("Amplitud")
plt.title("Amplitud")
plt.axhline(y=0, color="k")

plt.show();

#print(x)