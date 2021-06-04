n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

nums = sorted(nums, reverse=True)

for i in nums:
    print(i, end=' ')