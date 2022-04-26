N = 5
light = [0 for i in range(N)]
light

A = [1,3,4,2,5]

count = 1
for i in range(len(A)):
    turn = A[i] - 1
    light[turn] = 1

    if 0 in light:

        if light.index(0) >= sum(light):
            count += 1
            # print(i, light, light.index(0))
print(count)




def solution(A):
    # write your code in Python 3.6
    N = len(A)
    light = [0 for i in range(N)]
    count = 1

    for i in range(len(A)):
        turn = A[i] - 1
        light[turn] = 1

        if 0 in light:
            if light.index(0) >= sum(light):
                count += 1

    return count