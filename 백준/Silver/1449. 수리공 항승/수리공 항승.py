n, l = map(int, input().split())
water = list(map(int, input().split()))

water.sort()

cover = 0
num = 0
while water:
    tmp = water.pop(0)
    if tmp >= cover:
        cover = tmp + l
        num += 1

print(num)