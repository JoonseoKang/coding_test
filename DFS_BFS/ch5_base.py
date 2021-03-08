#Stack
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #젤 아래부터 출력
print(stack[::-1]) #젤 위에부터 출력

#Que
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

#recursive
def recursive_function():
    print('재귀 함수를 호출 합니다.')
    recursive_function()

recursive_function()

def recursive_function(i):
    if i == 100:
        return
        print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
        recursive_function(i + 1)
        print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

def factorial_iterative(n):
    result = 1

    for i in range(1, n+1):
        result *= i
    return result

print(factorial_iterative(5))


def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n -1)

print(factorial_recursive(5))

INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))


#DFS_BFS
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

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

visited = [False] * 9

dfs(graph, 1, visited)

#BFS
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

visited = [False] * 9

bfs(graph, 1, visited)


# stack
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])

#queue
from collections import deque #list로 하면 시간복잡도가 증가 함 그래서 deque 사용

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

#Recursive Function
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()


#종료 조건을 반도시 명시해야 함
#아니면 무한히 호출 되서 에러 또는 이상한 결과나올 수 있음
def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('iter:', factorial_iterative(5))
print('recursive:', factorial_recursive(5))

#최대 공약수
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))