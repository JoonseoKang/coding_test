n, m = map(int,input().split())

d = []
for i in range(n):
    d.append(list(map(int, input().split())))

chi = []
house = []
for i in range(n):
    for j in range(n):
        if d[i][j] == 1:
            house.append([i,j])
        if d[i][j] == 2:
            chi.append([i,j,0])


if m != 1:
    dis = []
    for i in house:
        tmp = []
        for j in chi:
            # print(i, j)
            distance = abs(i[0] - j[0]) + abs(i[1] - j[1])
            tmp.append(distance)
        dis.append(tmp)

    mini = []
    for i in dis:
        t = []
        for j in range(m):
            num = i.pop(i.index(min(i)))
            t.append(num)
        mini.append(t)

    count = 0
    for i in mini:
        count += min(i)

    print(count)

else:
    dis = []
    for i in chi:
        tmp = []
        for j in house:
            # print(i, j)
            distance = abs(i[0] - j[0]) + abs(i[1] - j[1])
            tmp.append(distance)
        dis.append(tmp)

    tt = []
    for i in dis:
        tt.append(sum(i))

    print(min(tt))
# dis
#
# for i in dis:
#     print(sum(i))

# tm = [2,3,5,2,7]
# tm.index(min(tm))
#
# tm.pop(tm.index(min(tm)))
# tm

# from itertools import combinations
# candidate = list(combinations(chi, m))