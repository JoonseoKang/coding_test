a = input()

digit = [str(i) for i in range(10)]

num =[]
liter = []
for i in a:
    if i in digit:
        num.append(i)
    else:
        liter.append(i)

s_liter = sorted(liter)

num = map(int, num)


s_liter.append(sum(num))

for i in s_liter:
    print(i, end='')