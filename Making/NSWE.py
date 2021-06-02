n = int(input())
move = list(input().split())

starting = [1, 1]

# R L U D
x = [0, 0, -1, 1]
y = [1, -1, 0, 0]


for i in move:
    if i == 'R' and starting[1] < n:
        starting[0] += x[0]
        starting[1] += y[0]
    elif i == 'L' and starting[1] > 1:
        starting[0] += x[1]
        starting[1] += y[1]
    elif i == 'U' and starting[0] > 1:
        starting[0] += x[2]
        starting[1] += y[2]
    elif i == 'D' and starting[0] < n:
        starting[0] += x[3]
        starting[1] += y[3]

print(starting[0], starting[1])