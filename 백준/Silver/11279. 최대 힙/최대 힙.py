import heapq

heap = []

n = int(input())
nums = [int(input()) for _ in range(n)]

for num in nums:
    if num == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -num)
