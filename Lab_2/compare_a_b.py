# -*- coding: utf-8 -*-

# Данный сценарий сравнивает два целых числа,
# и опередляет наименьшее из двух чисел, или же
# их равенство

a = input(u'Input integer a: ')
b = input(u'Input integer b: ')
if a<b:
    print 'a - the smallest of two numbers'
elif a==b:
    print 'a and b are equal'
else:
    print 'b - the smallest of two numbers'