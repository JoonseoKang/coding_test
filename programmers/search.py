from itertools import combinations
from itertools import permutations
from itertools import product
numbers = "011"
num = list(numbers)

list(product(*num))

t = []
for i in range(1,len(numbers)):
    k = list(permutations(num, i+1))
    for j in k:
        num.append(j)
num

t =[]
for i in num:
    tmp = []
    for j in i:
        tmp.append(j)
    t.append(tmp)

r = []
for i in t:
    a =''
    for j in i:
        a += j
    r.append(int(a))

answer = 0
for i in r:
    if i > 1:
        for j in range(2, i+1):
            if  i // j == 0:
                div = j
            if i == j:
                answer += 1


print(answer)

tt = []
for i in t:
    tt.append(''.join(i))

nums = [1,2,3,4]
combi = list(combinations(nums, 2))


