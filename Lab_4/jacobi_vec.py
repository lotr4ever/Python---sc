# -*- coding: utf-8 -*-

import time
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot


def jacobi(A, b, N=25, x=None):
    if x is None:
        x = zeros(len(A[0]))

    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times
    for i in range(N):
        x = (b - dot(R, x)) / D
    return x


if __name__ == '__main__':

    start_time = time.time()
    A = array([[2., -3., 0., 0.],
               [1., 2., -3., 0.],
               [0., 1., 2., -3.],
               [0., 0., 1., 2.]])
    b = array([-1., 0., 0., 3.])

    sol = jacobi(A, b, 1000)

    print "A:"
    pprint(A)

    print "b:"
    pprint(b)

    print "x:"
    pprint(sol)
    print("--- {} seconds ---".format(time.time() - start_time))