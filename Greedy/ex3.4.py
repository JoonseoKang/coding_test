n, k = map(int, input().split())

c = 0
while True:
    if n % k == 0:
        n /= k
        c += 1
    else:
        n -= 1
        c += 1


    if n == 1:
        break

print(c)