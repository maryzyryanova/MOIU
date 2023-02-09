import numpy

def change_rows(m: numpy.matrix, x: numpy.matrix, column: int) -> numpy.matrix:
    column -= 1
    for c in range(len(x)):
        m[c, column] = x[c, 0]
    return m


