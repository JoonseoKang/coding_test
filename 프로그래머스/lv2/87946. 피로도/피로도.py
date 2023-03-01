from itertools import permutations

def solution(k, dungeons):
    answer = -1
    combi = list(permutations(dungeons, len(dungeons)))
    
    for i in combi:
        tmp_k = k
        tmp = 0
        for j in i:
            if j[0] > tmp_k:
                continue
            else:
                tmp_k -= j[1]
                tmp += 1


        answer = max(answer, tmp)
    
    return answer