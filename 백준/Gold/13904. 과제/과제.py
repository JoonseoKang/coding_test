n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

dp.sort()

d = []
answer = 0

for date in range(n, 0, -1):
    while dp and dp[-1][0] >= date:
        d.append(dp.pop()[1])

    if d:
        d.sort()
        answer += d.pop()
        
print(answer)