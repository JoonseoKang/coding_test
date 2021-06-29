s = input()
sorted(list(s))

num = []
for i in range(10):
    num.append(str(i))

nums = 0
for i in sorted(list(s)):
    if i in num:
        nums += int(i)
    else:
        print(i, end='')
print(nums)