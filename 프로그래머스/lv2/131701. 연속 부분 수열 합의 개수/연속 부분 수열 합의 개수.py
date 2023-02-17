from itertools import combinations

def solution(elements):
    answer = []
    n = len(elements)
    elements *= 2
    # print(elements)
    
    for i in range(1, n+1):
        tmp = []
        for j in range(n):
            tmp.append(sum(elements[j:j+i]))
        
        
        answer.append(list(set(tmp)))
    
    answer = list(sum(answer, []))
        
    return len(set(answer))