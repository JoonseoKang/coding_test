
n = int(input())
location = list(map(int, input().split()))


location.sort()
#
num = (n-1)//2
print(location[num])
# l = [99999] * n
#
# count = 0
# for i in location:
#     count += (abs(i - location[num]))
#
# l[num] = count
#
# for i in range(1,3):
#     minus = num - i
#     plus = num + i
#     if minus < 0 or plus >= n:
#         break
#     else:
#         count = 0
#         cc = 0
#         for i in location:
#             count += (abs(i - location[minus]))
#             cc += (abs(i - location[plus]))
#
#         if count <= l[num]:
#             l[minus] = count
#         elif cc <= l[num]:
#             l[plus] = cc
#
#         else:
#             break
#
# # 1 2 3 4 4 4
# # 3 2 1 0 0 0
# # 2 1 0 1 1 1
# location[l.index(min(l))]