d = [[1, 0], [0, 1]]
t = int(input())

for _ in range(t):
    n = int(input())

    if n < len(d):
        print((' '.join(map(str, d[n]))))
    else:
        for i in range(len(d), n+1):
            now = [x + y for x, y in zip(d[i-2], d[i-1])]
            d.append(now)

        print((' '.join(map(str, d[n]))))

