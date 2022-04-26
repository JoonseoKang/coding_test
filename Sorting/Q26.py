# n = int(input())
# count = []
# for i in range(n):
#     count.append(int(input()))
#
# count.sort()
#
# # 10 + 20 = 30 [40]
# new_num = 0
#
# for i in range(len(count)-1):
#     new_num += count.pop(0) + count.pop(0)
#     count.insert(0, new_num)
#
# print(new_num)

import heapq

n = int(input())
heap = []
for i in range(n):
    data= int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)