
import heapq
import sys


def is_empty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True


T = int(input())

for _ in range(T):
    min_heap = []
    max_heap = []
    nums = dict()
    k = int(input())
    
    for j in range(k):
        com, n = sys.stdin.readline().split()
        num = int(n)
        
        if com == 'I':
            if num in nums:
                nums[num] += 1
            
            else:
                nums[num] = 1
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)
                
        elif com == 'D':
            if not is_empty(nums.items()):
                if num == 1:
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        tmp = -heapq.heappop(max_heap)
                        if tmp in nums:
                            del(nums[tmp])
                    nums[-max_heap[0]] -= 1
                
                else:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        tmp = heapq.heappop(min_heap)
                        if tmp in nums:
                            del(nums[tmp])
                    nums[min_heap[0]] -= 1
    
    if is_empty(nums.items()):
        print('EMPTY')
    else:
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        
        print(-max_heap[0], min_heap[0])
                
    