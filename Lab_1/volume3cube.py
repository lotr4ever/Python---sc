# -*- coding: utf-8 -*-

from numpy import linspace
import matplotlib.pyplot as plot

L=linspace(1,3,3)
V=L**3
print V

plot.plot(L, V)
plot.xlabel('L')
plot.ylabel('V')
plot.show()