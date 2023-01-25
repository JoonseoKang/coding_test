n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

answer = 0
for i in range(1, n+1):

    if coin[-i] <= k:
        a = k // coin[-i]
        answer += a
        k -= coin[-i] * a

    if k == 0:
        print(answer)
        break