s = int(input())
answer = 0
n = 0

for i in range(1, s+1):
    answer += i
    n += 1
    if answer > s:
        n -= 1
        break

print(n)