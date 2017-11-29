import math
import numpy as np
import scipy.linalg as sla

#получение данных соответствующих условию
def get_matrix(n):
    temp = np.ones(n - 1) * -1
    A = np.diag(np.ones(n) * 2) + np.diag(temp, k=-1) + np.diag(temp, k=1)
    return A


def get_b(n):
    b = np.zeros(n)
    h = 1. / n
    for i in range(n):
        b[i] = 2 * h * h
    return b


def get_x(n):
    x = np.zeros(n)
    h = 1. / n
    for i in range(1, n + 1):
        x[i - 1] = i * h * (1 - i * h)
    return x

# вспомогательная функция
def multiplication_diagonal(L):
    result = 1
    for i in range(len(L)):
        result *= L[i, i]
    return result


def lu3(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.eye(n)
    L[0, 0] = A[0, 0]
    U[0, 1] = A[0, 1] * 1. / L[0, 0]

    for i in range(0, n - 2):
        L[i + 1, i] = A[i + 1, i]
        L[i + 1, i + 1] = A[i + 1, i + 1] - L[i + 1, i] * U[i, i + 1]
        U[i + 1, i + 2] = A[i + 1, i + 2] * 1. / L[i + 1, i + 1]

    L[n - 1, n - 2] = A[n - 1, n - 2]
    L[n - 1, n - 1] = A[n - 1, n - 1] - L[n - 1, n - 2] * U[n - 2, n - 1]

    return L, U


def get_det_lu3(A):
    L, U = lu3(A)
    return multiplication_diagonal(L)

# вспомогательная функция
def first_step(L, b):
    n = len(b)
    y = np.zeros(n)
    y[0] = b[0] / L[0, 0]

    for i in range(1, n):
        y[i] = (b[i] - L[i, i - 1] * y[i - 1]) / L[i, i]

    return y

 # вспомогательная функция
def second_step(U, y):
    n = len(y)
    x = np.zeros(n)
    x[-1] = y[-1]
    for i in range(n - 2, -1, -1):
        x[i] = y[i] - U[i, i + 1] * x[i + 1]
    return x


def resolve_lu3(A, b):
    L, U = lu3(A)
    y = first_step(L, b)
    x = second_step(U, y)
    return x


if __name__ == '__main__':
    print('Введите размероность:')
    n = int(input())

    A = get_matrix(n)
    L, U = lu3(A)
    b = get_b(n)
    x = get_x(n)
    x_lu = resolve_lu3(A, b)

    print('Невязка для LU решения: {}'.format(sla.norm(A.dot(x_lu) - b)))
    print('Невявзка для ответ из условия: {}'.format(sla.norm(A.dot(x) - b)))

    print('Решение из условия:\n{} \nРешение через LU разложение:\n {}'.format(x, x_lu))

    print('Определитель матрицы полученный в LU: {}'.format(multiplication_diagonal(L)))
    print('Определитель полученный библиотечно: {}'.format(sla.det(A)))
