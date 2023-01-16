n = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1
for x in coin:
    if target < x:
        break
    target += x

print(target)
# 1 = 1 [1 2 3 9]
# 2 = 2 [1 3 9]
# 3 = 3 [1 9]
# 4 = 1 + 3 [9]
# 5 = 2 + 3
# 6 = 2 + 4
# 7 = 3 + 4
# 8 =
# 9
