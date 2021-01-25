n = input()


front = n[:int(len(n)/2)]
back =n[int(len(n)/2):]

front_sum = 0

for i in front:
    front_sum += int(i)

back_sum = 0

for j in back:
    back_sum += int(j)

if front_sum == back_sum:
    print('LUCKY')
else:
    print('READY')