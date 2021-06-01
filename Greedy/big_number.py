"""
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
배열의 특정한 인덱스가 연속 K번을 초과하여 더해질 수 없다
"""
import time
start_time = time.time()

n, m, k = map(int, input().split())
num = list(map(int,input().split()))

# 정렬해서 큰 수가 맨 앞에 오도록
s_num = sorted(num, reverse=True)

# s_num[0] * k + s_num[1] + s_num[0] *k + s_num[1]

result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += s_num[0]
#         m -= 1
#     if m == 0 :
#         break
#     result += s_num[1]
#     m -= 1
#
# print(result)


count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * s_num[0]
result += (m - count) * s_num[1]

print(result)

end_time = time.time()
print('time:', end_time - start_time)