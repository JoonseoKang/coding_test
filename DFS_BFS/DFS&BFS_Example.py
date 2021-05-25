"""
1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 0이면서 아직 방문하지 않은 지점을 방문
2. 방문한 지점에서 다시 상하좌우를 살펴보면서 방문을 진행하는 과정을 반복하면 연결된 모든 지점을 방문
3. 모든 노드에 대해서 1~2번의 과정을 반복, 방문하지 않은 지점의 수를 카운트
"""

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# x, y = 0, 0

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    else:
        #현재 노드를 아직 방문하지 않았다면
        if graph[x][y ] == 0:
            # 해당 노드 방문 처리
            graph[x][y] = 1
            # 상하좌우 위치들 모두 재귀적으로 호출
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
        return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

###example 4 미로탈출
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


dx = [1, -1, 0, 0] # 동 서 남 북
dy = [0, 0, 1, -1]

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))
