from collections import deque
n, m, k, x = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))


distance = [0] * (n+1)

def bfs(x):
    queue = deque()
    for i in graph:
        queue.append(i)

    while queue:
        a = queue.popleft()

        if x in a:
            for i in a:
                if i != x:
                    distance[i] = 1
        else:
            for i in a:
                if distance[i] == 0:
                    distance[i] = distance[a[0]] + 1

    return distance


distance = bfs(x)

result = []
for i in range(len(distance)):
    if distance[i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for j in result:
        print(j)


test = ')(()()(())(())'
test2 =')()('
test.count('(')
test.count(')')

for i in test:
    print(i)


def perfect_check(s):
    front = 0
    back = 0
    for i in s:
        if i == '(':
            front += 1
        else:
            back += 1

        if front < back:
            return -1
        else:
            return 0


perfect_check(test)
test2[1:-1]
len(test2)
test2[0:3]