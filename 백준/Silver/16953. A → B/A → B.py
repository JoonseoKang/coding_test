from collections import deque

a, b = map(int, input().split())

queue = deque([(a, 1)])
c = -1

while queue:
    n, t = queue.popleft()
   
    if n == b:
        c = t
        break
    
    if n*2 <= b:
        queue.append((n*2, t+1))
    if int(str(n)+'1') <= b:
        queue.append((int(str(n)+'1'), t+1))
    

print(c)