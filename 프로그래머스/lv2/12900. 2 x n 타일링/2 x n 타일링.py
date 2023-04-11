def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    prev_prev = 1
    prev = 2
    result = 0

    for i in range(3, n + 1):
        result = (prev_prev + prev) % 1000000007
        prev_prev = prev
        prev = result

    return result
