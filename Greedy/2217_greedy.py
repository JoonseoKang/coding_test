"""
https://www.acmicpc.net/problem/2217
"""

n = int(input())

weight = []
for i in range(n):
    weight.append(int(input()))

weight = sorted(weight)

max_weight = []
for i in range(n):
    max_weight.append((n-i) * weight[i])

print(max(max_weight))
