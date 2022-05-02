n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

d = [0] * (n)

d[0] = array[0]

tmp = []
for i in array[1]:
    tmp.append(d[0][0] + i)

d[1] = tmp


for i in range(2, n):
    tmp = [0] * len(array[i])
    for j in range(len(array[i])):

        if j == 0:
            tmp[j] = d[i-1][j] + array[i][j]
        elif j == i:
            tmp[-1] = d[i-1][-1] + array[i][-1]
        else:
            tmp[j] = max(d[i-1][j-1] + array[i][j], d[i-1][j] + array[i][j])
    d[i] = tmp

print(max(d[-1]))