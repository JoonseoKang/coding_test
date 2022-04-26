numbers = [3, 30, 34, 5, 9]

num = list(map(str, numbers))
num.sort(key = lambda x: x*3, reverse=True)
num

'3'*3 >'30' * 3
sorted(numbers, reverse=True)

tmp = []
for i in numbers:
    tmp.append(list(str(i)))

s = sorted(tmp, reverse=True)
s


t = ''
t = t + '3'
t += '5'
t
s
max(['3', '4'])

answer =''
for j in range(len(s) - 1):
    if s[j][0] == s[j+1][0]:
        if int(max(s[j])) <= int(max(s[j+1])):
            for k in s[j+1]:
                answer += k
            for kk in s[j]:
                answer += kk
        else:
            for k in s[j]:
                answer += k
    else:
        for i in s[j]:
            answer += i


answer

    for j in (list(str(i))):
        tmp.append(j)

answer = ''.join(sorted(tmp, reverse=True))