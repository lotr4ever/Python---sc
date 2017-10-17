# -*- coding: utf-8 -*-

from math import pi

r=10.6
a=1.3
b=1
carea=pi*r**2 

while carea > a*b:
    b+=1
    
b-=1

print 'Circle area:    ', carea
print 'Rectangle area: ', a*b 
print 'b: ',b