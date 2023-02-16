from collections import Counter
import math

def solution(str1, str2):
    answer = 0

    s1, s2 = [], []
    for idx, s in enumerate(str1):
        if idx <= len(str1) - 2:
            s1.append(str1.lower()[idx:idx+2])
    
    for idx, s in enumerate(str2):
        if idx <= len(str2) - 2:
            s2.append(str2.lower()[idx:idx+2])
    
    s1 = [char for char in s1 if char.isalpha()]
    s2 = [char for char in s2 if char.isalpha()]
    
    s1 = Counter(s1)
    s2 = Counter(s2)
    
    inter = list((s1 & s2).elements())
    union = list((s1 | s2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union)* 65536)
#     aob, aub = [], []
#     for i in s1:
#         for j in s2:
#             if i[0] == j[0]:
#                 if i[1] > j[1]:
#                     aub.append([i[0]] * i[1])
#                     aob.append([j[0]] * j[1])
#                 else:
#                     aob.append([i[0]] * i[1])
#                     aub.append([j[0]] * j[1])
                    
#     aob = sum(aob, [])
#     aub = sum(aub, [])
    
#     for i in s1:
#         if i[0] not in aub:
#             aub.append(i[0])
            
    
#     for i in s2:
#         if i[0] not in aub:
#             aub.append(i[0])
    

#     answer = len(aob) / len(aub)
#     answer *= 65536
#     answer = int(math.floor(answer))

    
    
    return answer