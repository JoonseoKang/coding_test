s = input()

make_0 = 0
make_1 = 0

if s[0] =='1':
    make_0 += 1
else:
    make_1 += 1


for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            make_0 += 1
        else:
            make_1 += 1


print(min(make_0, make_1))