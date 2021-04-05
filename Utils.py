from random import randint

MIN_VALUE = 1
MAX_VALUE = 10


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
