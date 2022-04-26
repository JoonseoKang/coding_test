n = int(input())

d = [0] * (n + 1)

d[0] = 1 # a1
d[1] = 3 # a2

for i in range(2, n):
    d[i] = d[i-1] + d[i-2] + 1

print(d[n - 1])
