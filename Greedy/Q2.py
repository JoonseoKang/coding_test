s = input()

sl = list(map(int, s))


result = 0

for i in range(len(sl)):
    if sl[i] <= 1 or result <= 1:
        result += sl[i]
    else:
        result *= sl[i]

print(result)