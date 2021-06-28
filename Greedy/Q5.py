n, m = map(int, input().split())
ball = list(map(int,input().split()))
ball.sort()

count = 0

for i in range(n-1):
    for j in range(n):
        if i < j and ball[i] != ball[j]:
            count +=1

print(count)