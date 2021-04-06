from copy import deepcopy
from random import randint
MIN_VALUE = 1
MAX_VALUE = 10


def determinant(matrix: list):
    d = 0
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - \
               (matrix[1][0] * matrix[0][1])

    for i in range(len(matrix)):
        curr_item = ((-1) ** i) * matrix[0][i] * \
                    determinant(new_matrix(matrix, 0, i))
        d += curr_item
    return d


def new_matrix(m: list, row, column):
    new = deepcopy(m)
    new.pop(row)
    for i in range(len(new)):
        new[i].pop(column)
    return new


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

def getL(matrix):
    raise NotImplementedError


def getU(matrix):
    raise NotImplementedError

# returns the solution of Ax=B using the invert method
def invertMethod(A, B):
    A_INVERT = invertMatrix(A)
    return multiplyMatrices(A_INVERT, B)


# returns the solution of Ax=B using the LU method
def LUMethod(A, B):
    L = getL(A)
    U = getU(L)
    L_INVERT = invertMatrix(L)
    U_INVERT = invertMatrix(U)
    return multiplyMatrices(multiplyMatrices(L_INVERT, U_INVERT), B)


def getMethod(A):
    return "Invert method" if isInvertible(A) else "LU method"

# prints matrix
def printMatrix(m):
    for row in m:
        print(row)


# creates a new matrix
# assign each value based on the range from MIN_VALUE and MAX_VALUE
def createMatrix(n):
    matrix = []
    for _ in range(n):
        item = []
        for _ in range(n):
            item.append(randint(MIN_VALUE, MAX_VALUE))
        matrix.append(item)
    return matrix


# checks if the given matrix is a squared matrix
# squared matrix => N x N
def isSquareMatrix(m):
    num_rows = len(m)
    for row in m:
        if len(row) != num_rows:
            return False
    return True

def main():

    # first, we create matrices A and B
    A = createMatrix(3)  # 3x3
    B = createMatrix(3)  # 3x3

    # second, we check if A is a squared matrix
    # otherwise, we have no point of proceeding..
    if not isSquareMatrix(A):
        print("A IS NOT A SQUARED MATRIX! EXITING...")
        exit(0)

    # finally, we check if A is invertible
    # if invertible, we use the standard Invert method
    # if A is not invertible, we use the LU decomposition method
    if isInvertible(A):
        X = invertMethod(A, B)
    else:
        X = LUMethod(A, B)

    print("The result of Ax=b is:")
    printMatrix(X)
    print(f"Solved using the {getMethod(A)}")


if __name__ == '__main__':
    main()
