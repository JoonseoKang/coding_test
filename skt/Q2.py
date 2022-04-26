n = 5
clockwise = True

a = [[1] * n for _ in range(n)]

a
# step1: n-2
for i in range(n-1):
    a[0][i] += i
    a[i][-1] += i
    a[-1][-1 - i] += i
    a[-1 - i][0] += i
i
# step2: n-3

for j in a[1:-1]:
    j[1:-1] = [n-1 for _ in range(3)]


for i in range(n-2):
    a[i][-2] += i
    a[1][i] += i
    a[-1-i][1] += i
    a[-2][-1-i] +=i

a
5 % 2

6//2
max(max(a))
a[2][2] = 7


