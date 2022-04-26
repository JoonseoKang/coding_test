'''
1. 다음 방향 변경 지점까지 거리 500m
or 출발 혹은 방향 변경 직후 다음 방향 변경 지점까지거리가 500m 이하
'''

# path1 = 'EEESEEEEEENNNN'
# list(path1)
#
# d = [0] * (len(path1) + 1)
#
# for i in range(len(path1)-1):
#     if path1[i] != path1[i+1]:
#         d[i+1] = 1
#
#
# index = list(filter(lambda x: d[x] == 1, range(len(d))))
# index.insert(0, 0)
#
# distance =[]
# direction = []

path1 = 'SSSSSSWWWNNNNNN'

d = [0] * (len(path1) + 1)


for i in range(len(path1)-1):
    if path1[i] != path1[i+1]:
        d[i+1] = 1

index = list(filter(lambda x: d2[x] == 1, range(len(d2))))

index
index.insert(0, 0)
index

distance=[]
for i in range(len(index) - 1):
    if index[i+1] - index[i] > 5:
        index[i] = index[i+1] - 5
        distance.append(5)

    else:
        distance.append(index[i+1] - index[i])


index
distance


turn = []

for i in range(len(index)):
    direction.append(path1[index[i]])

direction

for i in range(len(direction)-1):
    if direction[i] =='E' and direction[i+1] == 'S':
        turn.append('right')
    if direction[i] =='E' and direction[i+1] == 'N':
        turn.append('left')

    if direction[i] =='W' and direction[i+1] == 'S':
        turn.append('left')
    if direction[i] =='W' and direction[i+1] == 'N':
        turn.append('right')

    if direction[i] =='S' and direction[i+1] == 'W':
        turn.append('right')
    if direction[i] =='S' and direction[i+1] == 'E':
        turn.append('left')

    if direction[i] =='N' and direction[i+1] == 'W':
        turn.append('left')
    if direction[i] =='N' and direction[i+1] == 'E':
        turn.append('right')
turn
answer =[]
index
distance
turn

for i in range(len(distance)):
    answer.append('Time ' +str(index[i]) +': Go straight '+ str(distance[i]) + 'm and turn ' + turn[i])

answer

time = 1
navi = []
for i in index2:
    if i - time >= 5:
        navi.append(time)
        time = i - time
    else:
        navi.append(i)
        time = i

navi





for i in range(len(index2) - 1):
    if index2[i+1] - index2[i] >5:
        # index2.remove(i)
        index2[i] = index2[i+1] - 5

index2