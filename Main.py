from Invert import isInvertible
from Methods import invertMethod, LUMethod, getMethod
from Utils import *


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
