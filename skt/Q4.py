from collections import deque
from itertools import permutations
n = 5
edges = [[2,3],[0,1],[1,2]]

graph = [[] for _ in range(n+1)]

for i in edges:
    graph[i[0]].append(i[1])


def cal_dis(x):
    distance = [-1] * (n + 1)
    distance[x] = 0

    q = deque([x])
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                q.append(next_node)
    return distance


items = []
for i in range(n):
    items.append(i)

case = list(permutations(items, 3))


cal_dis(0)
cal_dis(1)
cal_dis(2)
cal_dis(3)
cal_dis(4)

answer = 0
for num in case:
    i, j, k = num[0], num[1], num[2]

    if i > j:
        first = cal_dis(j)[i]
    else:
        first = cal_dis(i)[j]
    if j > k:
        second = cal_dis(k)[j]
    else:
        second = cal_dis(j)[k]
    if i > k:
        plus = cal_dis(k)[i]
    else:
        plus = cal_dis(i)[k]

    if plus > 0 and second >0 and first >0:
        if plus == first + second:
            answer += 1


answer

cal_dis(0)


INF = int(1e9)
n = 5
m = 4

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

