array =[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end= ' ')


count

import math
math.floor(1.5)

N = 5
def my_f(x):
    if x < N:
        return x
    else:
        del x

a = [1,3,5,7,9]
list(map(my_f, a))

