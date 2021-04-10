from copy import deepcopy
from random import randint

MIN_VALUE = 1
MAX_VALUE = 10

# calculates the determinant of a matrix
def determinant(matrix: list):
    d = 0
    if len(matrix) == 2: # base case
        return (matrix[0][0] * matrix[1][1]) - \
               (matrix[1][0] * matrix[0][1])

    # we change the sign of each element(negative or positive)
    # and multiply it recursively with the smaller determinant with the new matrix
    for i in range(len(matrix)):
        curr_item = ((-1) ** i) * matrix[0][i] * \
                    determinant(new_matrix(matrix, 0, i))
        d += curr_item
    return d


# returns a new matrix minus the row and column given
def new_matrix(m: list, row, column):
    new = deepcopy(m)
    new.pop(row)
    for i in range(len(new)):
        new[i].pop(column)
    return new


# returns an identity matrix based on n size
def identityMatrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):  # assign 1 in the diagonal
        matrix[i][i] = 1
    return matrix

# returns true if a matrix is invertible (det != 0) else false
def isInvertible(matrix: list):
    return determinant(matrix) != 0


# returns the value of two multiply matrices accordingly (m1 * m2)
def multiplyMatrices(m1: list, m2: list):
    return [[sum(a * b for a, b in zip(m1_row, m2_col)) for m2_col in zip(*m2)]
            for m1_row in m1]


# returns the inverted A matrix
def invertMatrix(A):
    A_COPY = deepcopy(A)  # dont want to change the original A
    I = identityMatrix(len(A))
    indices = list(range(len(A)))

    for fd in range(len(A)):
        pivot = 1 / A_COPY[fd][fd]
        for j in range(len(A)):
            A_COPY[fd][j] *= pivot
            I[fd][j] *= pivot

        for i in indices[0:fd] + indices[fd + 1:]:
            crScaler = A_COPY[i][fd]
            for j in range(len(A)):
                A_COPY[i][j] = A_COPY[i][j] - crScaler * A_COPY[fd][j]
                I[i][j] = I[i][j] - crScaler * I[fd][j]
    return I


# returns the solution of Ax=B using the invert method
def invertMethod(A, B):
    A_INVERT = invertMatrix(A)
    X = multiplyMatrices(A_INVERT, B)
    print("The result is: ")
    printMatrix(X)


# returns the solution of Ax=B using the LU method
def LUMethod(A):
    # we create the first L matrix so we can continue to the next iterations
    matrix = deepcopy(A)
    elementary = identityMatrix(len(matrix))
    elementary[0][1] = (-1) * (matrix[0][1] / matrix[0][0])
    matrix = multiplyMatrices(elementary, matrix)
    L_MATRIX = invertMatrix(elementary)

    # we first check if the matrix is 2x2. if true, the L and U matrices already been found
    # otherwise, we proceed,
    if len(matrix) > 2:
        for i in range(len(matrix)):
            # we iterate over each pivot and over each item below the pivot in the column
            # for each item we create an elementary matrix and multiply the inverted elementary matrix with L
            pivot = matrix[i][i]

            for j in range(i + 1, len(matrix)):
                elementary = identityMatrix(len(matrix))
                elementary[i][j] = (-1) * (matrix[i][j] / pivot)
                matrix = multiplyMatrices(elementary, matrix)
                elementary_inverted = invertMatrix(elementary)
                L_MATRIX = multiplyMatrices(L_MATRIX, elementary_inverted)

    print("the L matrix: ")
    printMatrix(L_MATRIX)
    print("the U matrix: ")
    printMatrix(matrix)


# prints matrix
def printMatrix(m):
    for row in m:
        print([float("{:.2f}".format(item)) for item in row])


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
        print("USING THE INVERT METHOD\n")
        invertMethod(A, B)
    else:
        print("USING THE LU METHOD\n")
        LUMethod(A)


if __name__ == '__main__':
    main()
