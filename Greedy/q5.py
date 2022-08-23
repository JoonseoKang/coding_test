from itertools import combinations

n, m = map(int, input().split())
ball = list(map(int, input().split()))
combi = list(combinations(ball, 2))

c = 0
for i in combi:
    a, b = i[0], i[1]
    if a != b:
        c += 1

print(c)
