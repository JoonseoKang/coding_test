from itertools import product

numbers = [1,1,1,1,1]
l = [(x, -x) for x in numbers]
s = list(map(sum, product(*l)))
# -1 1 //2
# -2 0 2   // 3
# -3 -1 1 3 // 4
# -4 -2 0 2 4 //5
# -5 -3 -1 1 3 5 // 6

first = list(set(numbers))
d= []
for i in first:
    d.append(-i)
    d.append(i)

