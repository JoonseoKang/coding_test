from collections import deque

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]


def bfs(start, graph, num):
    queue = deque([start])
    visited.append(start)
    while queue:
        x, y = queue.popleft()
        graph[x][y] = num
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue

            else:
                if graph[nx][ny] != 0 and (nx, ny) not in visited:
                    graph[nx][ny] = graph[x][y]
                    visited.append((nx, ny))
                    queue.append((nx, ny))

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []
    check_list = []
    visited = []
    for i in range(h):
        tmp = list(map(int, input().split()))
        graph.append(tmp)


        for j in range(w):
            if tmp[j] == 1:
                check_list.append((i, j))

    num = 0
    for i in check_list:
        if i not in visited:
            num += 1
            bfs(i, graph, num)

    print(num)



