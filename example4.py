# 4-1
n = int(input())
data = list(input().split())

# 1,1  1,2 1,3 1,4  pass 2,4 3,4

x = 1
y = 1

for i in data:
    if y <= n and i == 'R':
        y += 1

    if y > 1 and i == 'L':
        y -= 1

    if x > 1 and i == 'U':
        x -= 1

    if x <= n and i == 'D':
        x += 1

print(x, y)


# 4-2
n = int(input())

result = 0

tmp = []
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            tmp.append(list(map(str,[i, j, k])))



for i in tmp:
    for j in i:
        if '3' in j:
            print(i)
            result += 1

print(result)
####답

n = int(input())

result = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                print(i,j,k)
                result += 1

print(result)


# 2
i = input()

cos = [(2,-1), (2,1), (-2,-1), (-2,1), (1,-2), (-1,-2), (1,2), (-1,2)]

if i[0] == ('a' or 'h') and i[1] == ('1' or '8') :
    count = len(cos) - 6

elif (i[0] == ('a' or 'h') and i[1] == ('2' or '7')) or (i[0] == ('b' or 'g') and i[1] == ('1' or '8')):
    count = len(cos) -5

elif (i[0] == ('c' or 'd' or 'e' or 'f') and i[1] == ('1' or '8')) or (i[0] == ('b' or 'g') and i[1] == ('2' or '7')) or(i[0] == ('a' or 'h') and i[1] == ('3' or '4' or '5' or '6')):
    count = len(cos) -2

else:
    count = len(cos)

print(count)


#답
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(2,-1), (2,1), (-2,-1), (-2,1), (1,-2), (-1,-2), (1,2), (-1,2)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


####4-3
n, m = map(int, input().split())
a, b, d = map(int, input().split())

minimap = []
for i in range(n):
    col = list(input().split())
    minimap.append(col)


xy = [a,b]

# d=0 -> d=3

if d != 0:
    d = d-1
else:
    d = 3

if minimap[a-1][b] == '1':
    if d != 0:
        d = d - 1
    else:
        d = 3
else:
    a = a-1

if d == 2:
    if minimap[a][b+1] == '1':
        if d != 0:
            d = d - 1
        else:
            d = 3
    else:
        b = b+1




#답
n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

#북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    #회전하고 앞에 안 가본칸이면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    #회전하고 정면에 안가본데가 없고 바다
    else:
        turn_time += 1

    #네 방향 다 못갈 때
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        #back
        if array[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break
        turn_time = 0

print(count)

















