stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

def recursive_func(i):
    if i == 100:
        return \
            print(i, 'th', i+1, '번째 재귀함수를 호출합니다.')
        recursive_func(i+1)
        print(i, '번째 재귀함수를 종료합니다')

recursive_func(1)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def dfs(graph, v, visited):
    #현재 노드 방문 처리
    visited[v] = 1
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [0] * 9

dfs(graph, 1, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                
visited = [0] * 9
bfs(graph, 1, visited)