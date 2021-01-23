n = int(input())
data = list(map(int, input().split(' ')))

data.sort()

#from 1

 #아니면 print(1) 리스트 중에 1이 있냐

# 2면 data[1:]에 1이나 2가 있냐  11 or 2
# 3 1,3이 있냐 111 12 3
# 4 1or 4 있냐 1111 112 13 4
# 5 1or 5 있냐 11111 1112 113 14 5
# 6 1or 6 있냐


# 1
# 11 2
# 111 21 3
# 1111 211 31 4
# 11111 2111 311 41 5

if 1 in data:
    print('is there')
    if 1 or 2 in data[1:]:
        print('hi')
        if 1 or 3 in data[2:]:
            print('dd')



result = 0

if data[0] != 1:
    result += 1
else:
    for i in range(10):
        if i >= len(data):
            pass
        else:
            if data[i+1] == 1 or i+1:
                result += 1

if data[2] == 1 or 2:
    print('ok')

print(result)


############풀이##########
"""
1. 처음에 금액 1을 만들 수 있는지 확인하려고 target =1로 설정한다
2. 1만들수 있으면 target=2로 업데이트
3. target=2를 만족하면 target= 2+2 = 4로 업데이트
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1

for x in data:
    if target < x:
        break
    target += x

print(target)