from itertools import combinations
[''.join(i) for i in set(list(permutations(['w', 'x', 'y', 'z'], 4)))]

from itertools import permutations
tmp = list(permutations(['w', 'x','y', 'z'], 4))
tmp

len(tmp)



tmp[0]
list('abca')
len(set(list(permutations(['a', 'b','c', 'a'], 4))))
set(list(permutations(['a', 'b','c', 'a'], 4)))
len('abca')
tmp = [''.join(i) for i in set(list(permutations(['a', 'b', 'c', 'a'], 4)))]
tmp.sort()
tmp

dup = []
for i in tmp:
    for j in range(len(i) -1):
        if i[j] == i[j+1]:
            print(i)
            dup.append(i)

result = []
for i in tmp:
    if i not in dup:
        print(i)
        result.append(i)

result
print(result)