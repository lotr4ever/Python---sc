# -*- coding: utf-8 -*-
# упражнение выполнено на python 3

import math
import numpy as np


def build_pascal_matrix(n):
    result = [[math.factorial(i + j) / math.factorial(i) / math.factorial(j)
               for j in range(n)] for i in range(n)]
    return result


def gauss(x):
    x = np.array(x, float)
    return x[1:] / x[0]


def gauss_app(C, t):
    C = np.array(C, float)
    t = np.array([[t[i]] for i in range(len(t))], float)
    C[1:, :] = C[1:, :] - t * C[0, :]
    return C


def build_lu_pascal_gauss(A):
    lu = np.array(A, float)
    for k in range(lu.shape[0] - 1):
        t = lu[k + 1:, k]
        lu[k:, k + 1:] = gauss_app(lu[k:, k + 1:], t)
    return lu


def build_lu_pascal_gauss_piv(A):
    lu = np.array(A, float)
    piv = np.array(range(lu.shape[0]))
    for k in range(lu.shape[0]):
        mu = k + np.argmax(A[k:, k])
        lu[[k, mu], :] = lu[[mu, k], :]
        piv[[k, mu]] = piv[[mu, k]]
        if lu[k, k] != 0:
            t = gauss(lu[k:, k])
            lu[k + 1:, k] = t
            lu[k:, k + 1:] = gauss_app(lu[k:, k + 1:], t)
    return lu, piv


def test_pascal_determinant():
    A = np.array(build_pascal_matrix(5))
    expected = 1
    computed = np.linalg.det(A)
    tol = 1e-14
    success = computed - expected < tol
    msg = 'x_exact = ' + str(expected) + '; x_computed = ' + str(computed)
    assert success, msg
