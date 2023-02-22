n, m = map(int, input().split())
see = set()
hear = set()

for _ in range(n):
    see.add(input())

for _ in range(m):
    hear.add(input())




ans = list(see & hear)
ans.sort()

print(len(ans))
for i in ans:
    print(i)