n = int(input())
move = list(input().split())

start_x, start_y = 1, 1


def moving(s, start_x, start_y):
    if s == 'R':
        start_x += 1
    if s == 'L':
        start_x -= 1
    if s == 'U':
        start_y -= 1
    if s == 'D':
        start_y += 1

    return start_x, start_y

for i in move:
    new_x, new_y = moving(i, start_x, start_y)
    # print(new_x, new_y)
    if new_x == 0 or new_y == 0 or new_x > n or new_y > n:
        pass

    else:
        start_x, start_y = new_x, new_y


print(start_y, start_x)
