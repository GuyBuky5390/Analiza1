from Determinant import *


def identityMatrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    j = 0
    for i in range(n):
        matrix[i][j] = 1
        j += 1
    return matrix


def isInvertible(matrix):
    return determinant(matrix) != 0


def multiplyMatrices(m1, m2):
    return [[sum(a * b for a, b in zip(m1_row, m2_col)) for m2_col in zip(*m2)]
            for m1_row in m1]


def invertMatrix(A):
    A_COPY = deepcopy(A)
    I = identityMatrix(len(A))
    I_COPY = deepcopy(I)
    indices = list(range(len(A)))

    for fd in range(len(A)):
        fdScaler = 1 / A_COPY[fd][fd]
        for j in range(len(A)):
            A_COPY[fd][j] *= fdScaler
            I_COPY[fd][j] *= fdScaler

        for i in indices[0:fd] + indices[fd + 1:]:
            crScaler = A_COPY[i][fd]
            for j in range(len(A)):
                A_COPY[i][j] = A_COPY[i][j] - crScaler * A_COPY[fd][j]
                I_COPY[i][j] = I_COPY[i][j] - crScaler * I_COPY[fd][j]
    return I_COPY
