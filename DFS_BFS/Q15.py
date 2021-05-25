# 모든 도로의 거리가 1이라는 것 때문에 BFS로 하면 간단히 해결 가능 함
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
        
if check == False:
    print(-1)