# https://www.acmicpc.net/problem/11399

n = int(input()) #사람의 수
p = list(map(int, input().split())) #P_i 인출 하는데 걸리는 시간

p = sorted(p)

tmp = []
count = 0
for i in range(n):
    count += p[i]
    tmp.append(count)

print(sum(tmp))