n = int(input())
t, p = [], []

for i in range(n):
    tmp = list(map(int, input().split()))
    t.append(tmp[0])
    p.append(tmp[1])


dp = [0] * (n+1)
max_value = 0


for i in range(n-1, -1, -1):
    time = t[i] - 1

    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]

    else:
        dp[i] = max_value


print(max_value)