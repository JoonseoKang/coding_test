n = int(input())

point = []
for _ in range(n):
    point.append(int(input()))

answer = 0
for i in range(n-1, 0, -1):
    if point[i] <= point[i-1]:
        answer += (point[i-1] - point[i] + 1)
        point[i-1] = point[i] - 1

print(answer)