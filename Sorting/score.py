n = int(input())

score =[]
for i in range(n):
    tmp = input().split(' ')
    score.append([tmp[0], int(tmp[1])])

score.sort(key = lambda x: x[1])

for i in score:
    print(i[0], end=' ')