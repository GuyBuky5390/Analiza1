from copy import deepcopy


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
