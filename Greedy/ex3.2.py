n, m, k = list(map(int, input().split()))
num = list(map(int, input().split()))

num.sort(reverse=True)

answer = 0
c = 0
for i in range(m):
    c += 1
    if c == k:
        answer += num[1]
        c = 0
    else:
        answer += num[0]

print(answer)