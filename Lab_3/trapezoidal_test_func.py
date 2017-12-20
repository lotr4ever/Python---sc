# -*- coding: utf-8 -*-
# упражнение выполнено на Python 3


manual_calc = 44


def trapezoidal(f, a, b, n):
	
	h = float(b - a)/n
	result = 0.5*(f(a) + f(b))
	for i in range(1, n):
		result += f(a + i*h)
	result *= h
	return result


def test_func():
    res = trapezoidal(lambda x: 2 * (x ** 3), 1, 3, 2)
    print('Результат функции: {}'.format(res))
    print('Совпадают ли вычисления: {}'.format(res == manual_calc))


test_func()