# -*- coding: utf-8 -*-

from math import pi

def c(r):
    C=2*pi*r
    return C

def a(r):
    A=pi*r**2
    return A

r = input(u'Input radius: ')

print 'Circumference:    ', c(r)
print 'Area of a circle: ', a(r)

r=1
print 'Circumference (r=1):    ', c(r)
print 'Area of a circle (r=1): ', a(r)