def solution(n, s):
    answer = []
    
    if s < n:
        return [-1]
    
    answer = [s//n for i in range(n)]
    idx = n - 1
    
    for i in range(s-sum(answer)):
        answer[idx] += 1
        idx -= 1
        
    return answer