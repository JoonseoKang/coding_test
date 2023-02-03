from itertools import combinations

def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while k and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    if k:
        stack = stack[:-k]
    answer = ''.join(stack)
    return answer