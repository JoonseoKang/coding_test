'''
문자데이터에서 가장 많이 등장하는 길이 1이상의 패턴 모두 삭제
대소문자 구분 X
여러개일 경우 모두 삭제
'''
from itertools import product, permutations
from collections import Counter
import itertools

call = 'abcabcdefabc'

call = call.lower()

w = list(set(list(call)))
w.sort()

len(list(permutations(w, 2)))
len(list(permutations(w, 3)))
len(list(permutations(w, 4)))

len(list(permutations(w, 5)))

tmp = list(permutations(w, 3))
tmp
tmp[0]

s = ''
for i in tmp[0]:
    s += i

len(s)
call[:len(s)]

count = 0
c =[]
for i in range(len(call)):
    if call[i:i+len(s)] ==s:
        count += 1


c.append([count, s])
len(call) // 2

call2 = 'ABCabcA'
call2 = call2.lower()
tmp = Counter(call2).most_common()
tmp[0]


most = []
num = tmp[0][1]
for i in tmp:
    if i[1] == num:
        most.append(i[0])


most

combi =[]
for i in range(len(most)):
    combi.append(list(map(''.join, permutations(most, i+1))))


combi = list(itertools.chain(*combi))

max_num = []
for i in combi:
    number_i = len(i)
    count = 0
    for j in range(len(call2)):
        if call2[j:j+number_i] == i:
            count += 1
    max_num.append([count,len(i), i])

max_num.sort(reverse=True)
max_num

m = max_num[0][0]
l = max_num[0][1]

my = []
for i in max_num:
    if i[0] == m and i[1] == l:
        my.append(i[2])
my
answer = call2
answer


for i in my:
    answer = answer.replace(i, '')
answer

t = call2.replace(my[0], '')

t.replace(my[1], '')