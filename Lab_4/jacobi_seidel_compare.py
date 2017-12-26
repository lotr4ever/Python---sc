# -*- coding: utf-8 -*-

from numpy import zeros
from pprint import pprint

from jacobi_vec import jacobi
from seidel import seidel


def build_task(n, a):
    A = zeros((n,n))
    b = zeros(n)
    b[0] = 1 - a
    b[n-1] = 1 + a
    for i in range(n):
        A[i][i] = a
        if i != n-1:
            A[i][i+1] = -1 - a
        if i != 0:
            A[i][i-1] = -1 + a
    for i in range(1, n-1):
        b[i] = 0
        return A, b

if __name__ == '__main__':
    eps = 1e-8
    n = input("Enter size of matrix \n")
    a = input("Enter number a \n")
    A, b = build_task(n, a)
    x_seidel, it_seidel = seidel(A, b, 1000)
    x_jacobi = jacobi(A, b, 1000)
    print "A:"
    pprint(A)

    print "b:"
    pprint(b)

    print "x:"
    pprint(x_jacobi)
    pprint(x_seidel)