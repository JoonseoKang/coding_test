n = int(input())

num = list(str(n))
# int(len(num) / 2)

a = list(map(int, num[0:int(len(num) / 2)]))
b = list(map(int, num[int(len(num) / 2):]))

if sum(a) == sum(b):
    print('LUCKY')
else:
    print('READY')