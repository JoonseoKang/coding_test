n = int(input())
array = list(map(int, input().split()))

# a1 + a3 < a2 + a4


d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])
#a1 < a2 -> a2 start

