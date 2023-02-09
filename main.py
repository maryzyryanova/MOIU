import numpy as np
from lab_1 import change_rows

A = np.matrix([
    [1, -1, 0],
    [0, 1, 0],
    [0, 0, 1]])

A_opposit = np.linalg.inv(A)

Q = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
x = np.matrix([[1], [0], [1]])
i = 3

B = change_rows(A, x[:, 0], i)

l = A_opposit*x

l_new = l.copy()
l_new[i-1] = -1


l_vect = -l_new/l[i-1]
Q_new = change_rows(Q, l_vect, i)
result = Q_new.dot(A_opposit)
print(result)