n = int(input())
pear = list(map(int, input().split()))

pear.sort()


result = 0
count = 0

for i in pear:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
