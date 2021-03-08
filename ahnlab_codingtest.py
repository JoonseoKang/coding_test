import os

((20//30)+1) * 30

((40//30)+1)*30

means(1,3,5)

mails = [9, 20, 10, 30, 23, 4]

count = 0
for i in range(len(mails)-3+1):
    print(i)


sum(mails[0:3]) / 3
sum(mails[1:4]) / 3

env = [[2, 3], [4, 5], [3, 4]]
env
env.sort()
env[0][1]

count = 0
for i in range(len(env)-1):
    if env[i][0] < env[i+1][0] and env[i][1] < env[i+1][1]:
        count += 1

print(count)

i = 0
j = 1
answer = 0
while True:

    if i == len(env) or j == len(env):
        break
    else:
        if env[i][0] < env[j][0] and env[i][1] < env[j][1]:
            answer += 1
            i += 1
            j = i + 1

        else:
            j += 1




answer

    else:
        j += 1
        if env[i][0] < env[j][0] and env[i][1] < env[j][1]:
            count += 1