import numpy as np

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

key = np.array(key)


b = np.array(key).T

a = np.array(key)
a
a[:,2] = a[0]
a
a[:,1] = a[1]
print(b.T)
#회전
new_key = key

key[2]

def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0 * n for _ in range(m)]]
    for i in range(n):
        for j in range(m):
            result[j][n -i -1] = a[i][j]
    return result

a = rotate_a_matrix_by_90_degree(key)

def solution(key, lock):
    answer = True
    return answer