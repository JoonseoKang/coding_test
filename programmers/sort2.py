c = [3, 0, 6, 1, 5]
c.sort(reverse=True)
c
c[0] > 0

tmp = 0
for i in c:
    if i >= 0:
        tmp += 1
print(tmp)

c
for i in reversed(range(len(c))):
    paper = 0
    tmp = []

    for j in c:
        if j >= i+1:
            paper += 1

        else:
            tmp.append(j)


    if paper >= i + 1:
        if sum(tmp) <= i+1:
            h = i+1
            break
        else:
            pass
    else:
        pass

h