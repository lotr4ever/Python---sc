# -*- coding: utf-8 -*-
import numpy as np
import math


def get_Gilbert_matrix(size):
    A = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            A[i, j] = 1 / (i + j + 1)

    return A


def cholesky(A):
    n = A.shape[0]
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            L[i, j] = (A[i, j] - sum(L[i, :j]*L[j, :j])) / L[j, j]

        L[i, i] = math.sqrt(A[i, i] - sum(L[i, :i] ** 2))
    return L


def det_cholesky(L):
    return np.product(L[np.diag_indices(len(L))] ** 2)


if __name__ == '__main__':
    n = 4
    A = get_Gilbert_matrix(n)
    C = np.linalg.cholesky(A)
    L = cholesky(A)
    print('Норма разности A- LL^T: ', np.linalg.norm(A - L.dot(L.transpose())))
    print('L=', L)
    print('Определитель матрицы, высчитанный по Холецкому: ', det_cholesky(L))
