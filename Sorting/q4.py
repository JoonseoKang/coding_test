from collections import deque
n = int(input())
card=[]
for i in range(n):
    card.append(int(input()))

card.sort()

q = deque(card)

num = q.popleft()

for i in range(n-1):
    num += q.popleft()
    q.insert(0, num)

print(sum(q))