import numpy as np
from lab_2 import (
    symplex,
    basis_matrix
)

def correct_vector(b: list, A: list):
    for i in range(0, len(b)):
        if b[i] < 0:
            A[i] = 0
            b[i] = 0
    return b, A

def create_vector(m: int, n: int):
    new_vector = []
    for i in range(0, n):
        new_vector.append(0)
    for i in range(0, m):
        new_vector.append(-1)
    return new_vector

def create_matrix(m: int):
    new_vector = np.zeros((m, m))
    for i in range(0, m, 1):
        new_vector[i][i] = 1
    return new_vector

def create_x(n: int, b: list):
    x = np.zeros((1, n))
    b = np.transpose(b)
    return np.hstack([x, b])

def create_B(n: int, m: int):
    B = []
    for i in range(1, m+1):
        B.append(n+i)
    return B

def find_max_B(B: list):
    _max = -1e20
    _pos: int
    for i in range(len(B)):
        if B[i] > _max:
            _max = B[i]
            _pos = i
    return _max, _pos

def find_l(basisA, new_A: list, B: list, n: int):
    l = []
    for j in B:
        l.append(np.matmul(basisA, new_A[:, j-1]))
    return l

def delete_intersections(j: list , B: list):
    intersections = []
    new_B = []
    for i in j:
        for b in B:
            if i == b:
                intersections.append(i)
    for i in j:
        for item in intersections:
            if i != item:
                new_B.append(i)
    return new_B


if __name__ == "__main__":
    A = np.array([
        [1, 1, 1],
        [2, 2, 2]
    ])
    b = np.array([
        [0],
        [0]
    ])
    c = np.array([1, 0, 0])
    m = 2
    n = 3

    b, A = correct_vector(b, A)
    c_transported = create_vector(m, n)
    new_A = np.hstack([A, create_matrix(m)])
    x = create_x(n, b)
    B = create_B(n, m)

    print('-'*70)
    print('Матрица А после корректировки: ', A, sep="\n")
    print('Вектор b после корректировки: ', b, sep="\n")
    print('Вектор c коэффициентов переменных в целевом функционале: ', c_transported)
    print('Новая матрица А: ', new_A, sep="\n")
    print('Начальный базисный допустимый план задачи: ', 'x = ', x, ', B = ', B)

    basisA, x, B = symplex(new_A, B, c_transported, x) 
    _max, _pos = find_max_B(B)
    i = n - _pos
    j = [x for x in range(1, n+1)]
    new_B = delete_intersections(j, B)
    l = find_l(basisA, new_A, new_B, n)
    
    print('-'*70)
    print('Оптимальный план x: ', x)
    print('Множество базисных индексов B: ', B)
    print('Новый вектор B: ', new_B)

    k = 0
    flag = False
    for j in new_B:
        print(f'Вектор l({j}): ', l[k], sep="\n")
        if l[k][i-1] == 0:
            flag = True
        k += 1
    if flag == True:
        A = np.delete(A, (i-1), axis=0)
        new_A = np.delete(new_A, (i-1), axis=0)
        B = B.pop(0)
        b = np.delete(b, (i-1), axis=0)
    print('Итоговая матрица А: ' , A)
    print('Итоговая матрица new_A: ', new_A)
    print('Конечное множество базисных индексов В: ', B)
    print('Конечный допустимый план задачи: ', x[0:n])
    print('Конечный вектор b: ', b)
    
    

    