n = int(input())

c = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):

            time = list(str(i)+str(j)+str(k))
            # print(time)
            if '3' in time:
                c += 1

print(c)



