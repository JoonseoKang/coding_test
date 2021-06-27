s = input()

# 0001100 11에서 한 번
# 0101011 맨뒤 11에서 한 번 0101000 1,1 2번 뒤집어서 총 3번

# 전부 0으로 바꾸는 경우와 1로 바꾸는 경우를 비교
count0 = 0
count1 = 0

# 1st 원소처리
if s[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두번째 원소부터 모든 원소를 확인
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count0 += 1
        else:
            count1 += 1


print(min(count0, count1))