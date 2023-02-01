t = int(input())
for _ in range(t):
    n = int(input())
    tree = list(map(int, input().split()))

    tree.sort()
    d = [[] for _ in range(n)]
    start = n // 2
    d[start] = tree.pop()

    c = 0
    while tree:
        c += 1
        d[start - c] = tree.pop()
        if tree:
            d[start + c] = tree.pop()

    answer = abs(d[0] - d[-1])
    for i in range(n - 1):
        answer = max(answer, abs(d[i] - d[i+1]))

    print(answer)

