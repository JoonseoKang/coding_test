#https://www acmicpc net/problem/4796
i = 0
while True:
    l, p, v = map(int, input().split())
    i += 1

    if v == 0:
        break
    else:
        if l == p:
            n1 = l * (v // p)
            print('Case ' + str(i) + ': ' + str(n1))


        else:
            n1 = l * (v // p)
            n2 = v - (p * (v // p))
            num = n1 + n2
            print('Case ' + str(i) + ': ' + str(num))


