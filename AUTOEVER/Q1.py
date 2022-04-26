rooms = ["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"]
target = 403

# rooms

# rooms[0].split(']')[0].replace('[', '')

new_table = []
no_name = []
for i in rooms:
    front = i.split(']')[0].replace('[', '')
    back = i.split(']')[1].split(',')

    if int(front) != target:
        for j in back:
            new_table.append([j, front])
    else:
        no_name.append(back)

no_name[0]
new_table

for i in new_table:
    i.append(abs(int(i[1]) - target))

new_table

names = []
for i in new_table:
    if i[2] == 0:
        new_table.remove(i)
    names.append(i[0])

names

from collections import Counter
n = Counter(names)

# n['Azad']

for i in new_table:
    i.append(n[i[0]])

new_table.sort(key=lambda x: (x[3], x[2], x[0]))

new_table

for i in range(len(new_table) -1):
    if new_table[i][0] == new_table[i+1][0]:
        # print(new_table[i+1])
        new_table.pop(i+1)

new_table

answer = []
for i in new_table:
    answer.append(i[0])

answer

names = []
for i in new_table:
    if i[2] == 0:
        new_table.remove(i)
    else:
        names.append(i[0])

new_table

names
from collections import Counter
dict(Counter(names))



########################
rooms
target

for i in rooms:
    i = i.replace('[', '')
    i = i.replace(']', ' ')

    if int(i.split(' ')[0]) == target:
        print(i)