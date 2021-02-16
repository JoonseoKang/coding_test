def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0 * n for n in range(m)]]
    for i in range(n):
        for j in range(m):
            result[j][n -i -1] = a[i][j]
    return result


s= 'abc'
len(s)

5 // 3

s * 2 + s[:2]

a = 'world'

n, k = map(int, input().split())
price = list(map(int, input().split()))

price.sort()

num = 0

for i in price:
    k = k - i

    if k < 0:
        break

    else:
        num += 1

print(num)

tmp = [0 for i in range(3)]
tmp.sort()

a = [-1,5,-2]
a
list(map(abs, a))

a.sort()
a = 'cde'
b =  'abc'

set(a) & set(b)


for i in a:
    if i in set(a) & set(b):
        print(i)