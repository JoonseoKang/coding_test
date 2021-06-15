n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n+1)

for i in range(0, n+1):
    parent[i] = i

for i in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        union(parent, a, b)
    elif o == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('Yes')
        else:
            print('No')