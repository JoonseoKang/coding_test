"""
내림차순x, 오름차순으로 정렬
낮은 모험가 부터 하나씩 확인

"""

n = int(input())
data = list(map(int,input().split(' ')))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가 수

for i in data: # 공포도 낮은 것부터 하나씩
    count += 1 # 현재 그룹에 모험가 포함
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1
        count =0 # 그룹안의 모험가 수 초기화

print(result)

