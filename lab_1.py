import numpy as np

def change_rows(m: np.matrix, x: np.matrix, column: int) -> np.matrix:
    column -= 1
    for c in range(len(x)):
        m[c, column] = x[c, 0]
    return m


if __name__ == '__main__':
    A = np.matrix([
        [1, -1, 0],
        [0, 1, 0],
        [0, 0, 1]])
    print('Матрица А: ', A, sep='\n')

    A_opposit = np.linalg.inv(A)
    print('Матрица, обратная матрице А: ', A_opposit, sep='\n')

    Q = np.matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    print('Единичная матрица Q порядка 3: ', Q, sep='\n')

    x = np.matrix([[1], [0], [1]])
    print('Вектор х: ', x, sep='\n')

    i = 3
    B = change_rows(A, x[:, 0], i)
    print(f'В матрице А заменяем {i} столбец на столбец х. Получаем: ', B, sep='\n')

    l = A_opposit*x
    print('Вектор l: ', l, sep='\n')

    l_new = l.copy()
    l_new[i-1] = -1
    print('В копии вектора l заменим третий элемент на -1: ', l_new, sep='\n')

    l_vect = -l_new/l[i-1]
    print('Находим вектор l с шапочкой:', l_vect, sep='\n')

    Q = change_rows(Q, l_vect, i)
    print('Заменим в единичной матрице Q третий столбец на столбец l с крышечкой: ', Q, sep='\n')

    result = Q.dot(A_opposit)
    print('Наконец, находим матрицу обратную к матрице B', result, sep='\n')