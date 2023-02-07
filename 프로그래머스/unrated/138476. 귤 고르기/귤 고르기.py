from collections import Counter

def solution(k, tangerine):
    answer = 0
    c = Counter(tangerine)
    c = c.most_common()
    
    t = []
    for i in c:
        for _ in range(i[1]):
            if len(t) < k:
                t.append(i[0])
            else:
                break
            
            # print(t, len(t), k)
            

    answer = len(set(t))

    return answer