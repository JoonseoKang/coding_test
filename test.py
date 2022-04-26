arr = [['Apeach', 'Frodo', '5'], ['Frodo', 'Apeach', '3'], ['Tube', 'Apeach', '7'],\
['Tube', 'Apeach', '4'], ['Tube', 'Apeach', '2']]

arr[0][0]

dict = {}
arr[0][0]

arr[0][0:2]


tmp = []
for i in arr:
    tmp.append(i[0])
    tmp.append(i[1])

set(tmp)

t = [i[0] for i in arr]
t1 = [i[1] for i in arr]

t = list(set(t+t1))

dict = {}
dict = set(t+t1)
t[0]

for i in range(len(t)):
    dict[t[i]] = 0

dict={}
for i in arr:
    d = {}
    d[i[0]] = i[2]
    dict + d

import pandas as pd
df = pd.DataFrame(arr, columns=['a', 'b', 'c'])

df['c'] = pd.to_numeric(df['c'])

d1 = df.groupby('a')
d1 = d1.sum()['c']

d2 = df.groupby('b')
d2 =d2.sum()['c']

d3 = d2.sub(d1, fill_value=0)

name = list(d3.index)
money = list(d3)

dict ={}
for i in range(len(name)):
    dict[name[i]] = money[i]

2 >= 0

min(dict.values())

min(dict, key = lambda x: dict[x])


