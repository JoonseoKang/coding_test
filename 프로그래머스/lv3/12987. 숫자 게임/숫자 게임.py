from collections import deque

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    A = deque(A)
    B = deque(B)

    while A:
        tmp = A.popleft()
        while B:
            b = B.popleft()
            if tmp < b:
                answer += 1
                break
    return answer