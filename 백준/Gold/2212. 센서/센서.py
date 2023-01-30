n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

if k >= n:
    print(0)
    exit()
    
dist = []
for i in range(1, n):
    dist.append(sensor[i] - sensor[i-1])

dist.sort(reverse=True)
for _ in range(k-1):
    dist.pop(0)

print(sum(dist))