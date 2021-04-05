from Invert import invertMatrix, multiplyMatrices, isInvertible
from LU import getL, getU


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
