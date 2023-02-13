n, m = map(int, input().split())
location = list(map(int, input().split()))
minus = [x for x in location if x < 0]
plus = [x for x in location if x > 0]
plus.sort()
minus.sort(reverse=True)



answer = 0
if minus and plus:
    if abs(min(minus)) < max(plus):
        answer += max(plus)
        for _ in range(m):
            if plus:
                plus.pop()
    else:
        answer += abs(min(minus))
        for _ in range(m):
            if minus:
                minus.pop()

    c = 0
    tmp = []
    while minus:
        c += 1
        num = minus.pop()
        tmp.append(num)
        if c == m:
            answer += -tmp[0] * 2
            tmp = []
            c = 0

    if tmp:
        answer += -tmp[0] * 2

    c = 0
    tmp = []
    while plus:
        c += 1
        num = plus.pop()
        tmp.append(num)
        if c == m:
            answer += tmp[0] * 2
            tmp = []
            c = 0

    if tmp:
        answer += tmp[0] * 2

    # print(answer)

elif not minus:
    answer += max(plus)
    for _ in range(m):
        if plus:
            plus.pop()

    c = 0
    tmp = []
    while plus:
        c += 1
        num = plus.pop()
        tmp.append(num)
        if c == m:
            answer += tmp[0] * 2
            tmp = []
            c = 0

    if tmp:
        answer += tmp[0] * 2

else:
    answer += abs(min(minus))
    for _ in range(m):
        if minus:
            minus.pop()

    c = 0
    tmp = []
    while minus:
        c += 1
        num = minus.pop()
        tmp.append(num)
        if c == m:
            answer += -tmp[0] * 2
            tmp = []
            c = 0

    if tmp:
        answer += -tmp[0] * 2


print(answer)