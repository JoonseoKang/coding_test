s = input()

answer = 0
for i in s:
    num = int(i)
    if num == 0 or num == 1 or answer == 0:
        answer += num
    else:
        answer *= num

print(answer)
