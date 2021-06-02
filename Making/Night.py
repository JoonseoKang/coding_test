here = list(input())

result = 0
step = [(-2,-1), (-2,1), (-1,2), (-1,-2), (1,2), (1, -2), (2,1), (2,-1)]

here[0] = int(ord(here[0])) - int(ord('a')) + 1
here[1] = int(here[1])

for s in step:
    next_x = here[0] + s[0]
    next_y = here[1] + s[1]

    if next_x >= 1 and next_y <= 8 and next_x <=8 and next_y >= 1:
        result += 1

print(result)