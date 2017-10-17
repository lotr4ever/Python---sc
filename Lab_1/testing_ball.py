# -*- coding: utf-8 -*-
# Программа для вычисления положения мяча при вертикальном движении

v0 = 5       # Начальная скорость
g = 9.81     # Ускорение свободного падения
t = 0.6      # Время

y = v0*t - (1/2)*g*t**2

print y

# 1.
#    привет v0 = 5
#    ^
#SyntaxError: invalid syntax

# 2.
#    v0 = 5        Начальная скорость
#                  ^
#SyntaxError: invalid syntax

# 3.
#    v0  5       # Начальная скорость
#        ^
#SyntaxError: invalid syntax

# 4.
#    pint y
#         ^
#SyntaxError: invalid syntax

# 5.
# y = 3.0

# 6.
#    print x
#NameError: name 'x' is not defined

# 7.
# y = 3.0