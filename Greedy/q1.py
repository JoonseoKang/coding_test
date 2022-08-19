'''
공포도가 x인 모험가는 반드시 x명 이상으로 팀 구성
최대 몇 그룹?

answer
공포도가 낮은 모험가부터 하나씩 확인
현재 그룹에 포함된 모험가가 현재확인하고 있는 공포도보다 크거나 같으면 그룹 결성
'''

n = int(input())
pear = list(map(int, input().split()))

pear.sort()

c = 0
group = []
while pear:
    a = pear.pop(0)
    group.append(a)
    if len(group) == a:
        c += 1
        group = []

print(c)