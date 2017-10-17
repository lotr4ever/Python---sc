# -*- coding: utf-8 -*-

def average(N):
   n=range(N+1)
   s=sum(n)
   return s/N

N = input(u'Input N: ')

print 'Average: ',average(N)