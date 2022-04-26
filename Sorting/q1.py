n = int(input())

data = []
for i in range(n):
    data.append(list(input().split()))

data.sort(key = lambda x: (-int(x[1]), x[2], -int(x[3]), x[0]))
data