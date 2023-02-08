from collections import Counter

def solution(n):
    answer = 0
    now = bin(n)
    # print(bin(78), bin(83))
    num_one = Counter(now)['1']
    while True:
        n += 1
        if num_one == Counter(bin(n))['1']:
            # print(n, bin(n))
            return n
            break
        

def binary_num(x):
    len_bin = 1
    for i in range(1, 20):
        if 2 ** i < x:
            len_bin += 1
        else:
            break
            
    max_len = len_bin

    if x == 2 ** max_len:
        answer = ['0'] * max_len
        answer[0] = '1'
    else:
        answer = ['1'] * max_len
        x -= 2 ** (max_len - 1)

        for i in range(max_len-2, -1, -1):
            if 2 ** i <= x:
                x -= 2**i
            else:
                answer[-i-1] = '0'

    return ''.join(answer)