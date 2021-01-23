s = input()

# s[0] == s[1] #같으면 2번째
# s[1] == s[2]
# s[2] == s[3]
# s[3] == s[4]
# s[4] == s[5]
# s[5] == s[6]
# s[6] == s[7] #index 초과

result = 0

for i in range(len(s)):
    if i == len(s)-1:
        pass
    else:
        if s[i] != s[i+1]:
            result += 1

result = result -1

print(result)


#답변
data = input()
count0 =0 #all change 0
count1 = 0 #all change 1

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))