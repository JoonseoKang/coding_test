def solution(n, t, m, p):
    answer = ''
    tmp = ''
    
    for num in range(m*t):
        tmp += convert_notation(num, n)
    
    for i in range(p-1, m*t, m):
        answer += tmp[i]
    
    return answer

def convert_notation(n, base):
    if n == 0:
        return '0'
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]