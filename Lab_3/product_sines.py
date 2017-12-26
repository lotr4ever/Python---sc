# -*- coding: utf-8 -*-
# упражнение выполнено на python 3

from math import sin, pi
import matplotlib.pyplot as plt
import numpy as np


def trapezoidal(f, a, b, n):
    h = float(b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result


def adaptive_integration(f, a, b, eps, method='trapezoidal'):
    n = 1
    while abs(trapezoidal(f, a, b, n) - trapezoidal(f, a, b, 2 * n)) >= eps:
        n *= 2
    result = trapezoidal(f, a, b, 2 * n)

    return result


def product_sines():
    a = -pi
    b = pi
    eps = 1E-15
    for k in range(10):
        for j in range(10):
            v = lambda x: sin(j * x) * sin(k * x)
            print('k =', k, ', j =', j, ':',
                  adaptive_integration(v, a, b, eps))

product_sines()

x = np.linspace(-pi, pi, 1000)
y_1 = np.sin(x) * np.sin(x * 2)
y_2 = np.sin(x * 2) * np.sin(x * 3)

plt.plot(x, y_1)
plt.figure()
plt.plot(x, y_2)
plt.show()

#   Функции кусочно-симметричны относительно точек -pi/2 и pi/2,
# поэтому их интегралы, численно равные площади под графиком, равны нулю.
