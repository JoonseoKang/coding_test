n = 5

m = [[0] * (n) for _ in range(n)]
build_frame =  	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

build_frame[0]

x, y ,a ,b = build_frame[0]

5-y-1
m
m[n-1-y][x] = 1
m[n-1-y-1][x] = 1

x, y ,a ,b = build_frame[1]
if m[n-1-y][x] == 1:
    m[n - 1 - y][x+1] = 1

4-0

for i in build_frame:
    x, y, a, b = i

    if a == 1:
        if b == 1 and (y == 0 or m[n-1-y][x] == 1):
            if n - 1 - y - 1 >= 0:
                m[n - 1 - y][x] = 1
                m[n - 1 - y - 1][x] = 1

#CHECK 함수를 만들어서 설치나  삭제가 가능한지 확인해보는게 핵심