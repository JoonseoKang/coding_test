s = input()

result = 0


for i in range(len(s)):
    num = int(s[i])

    if num <= 1:  #1인경우도 고려해야 됨 1*2 = 2  // 1+2 =3

        if int(i) == len(s)-1:
            pass
        else:
            result += int(s[int(i) + 1])
    else:
        if int(i) == 0:
            result = num            # 첫항 고려해야 함

        if int(i) == len(s)-1:
            pass

        else:
            result *= int(s[int(i) + 1])

print(result)



####################################답안지#########################################

result2 = int(s[0])
for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or result2 <= 1:
        result2 += num
    else:
        result2 *= num