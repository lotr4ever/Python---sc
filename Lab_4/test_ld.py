# -*- coding: utf-8 -*-
# упражнение выполнено на python 3

import numpy as np


def build_kms_matrix(rho, n):
    return [[rho ** abs(i - j) for j in range(n)] for i in range(n)]


def ld(A):
    n = len(A)
    LD = np.array(A, float)
    for j in range(n):
        v = np.zeros(j + 1)
        v[:j] = LD[j, :j] * LD[range(j), range(j)]
        v[j] = LD[j, j] - np.dot(LD[j, :j], v[:j])
        LD[j, j] = v[j]
        LD[j + 1:, j] = (LD[j + 1:, j] - np.dot(LD[j + 1:, :j], v[:j])) / v[j]

    return LD

def ld_solve(A, b):
    LD = ld(A)
    b = np.array(b, float)
    for i in range(1, len(b)):
        b[i] = b[i] - np.dot(LD[i, :i], b[:i])
    b[:] = b[:] / LD[range(len(b)), range(len(b))]
    for i in range(len(b) - 1, -1, -1):
        b[i] = (b[i] - np.dot(LD[i + 1:, i], b[i + 1:]))
    return b


def test_ld_solve():
    A = np.array([[10, 20, 30], [20, 45, 80], [30, 80, 171]])
    expected = np.array([1, 1, 1], float)
    b = np.dot(A, expected)
    computed = ld_solve(A, b)
    tol = 1e-10
    success = np.linalg.norm(abs(expected - computed)) < tol
    msg = 'expected: ' + str(expected) + ', computed: ' + str(computed)
    assert success, msg


def test_kms_ld():
    rho = 4
    n = 5
    A = build_kms_matrix(rho, n)
    expected = np.full(n, 1 - rho ** 2)
    expected[0] = 1
    computed = np.diag(ld(A))
    success = np.allclose(computed, expected, atol=1e-10)
    msg = 'expected: ' + str(expected) + ', computed: ' + str(computed)
    assert success, msg
