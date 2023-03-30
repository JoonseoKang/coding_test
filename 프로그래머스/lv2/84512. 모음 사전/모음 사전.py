from itertools import combinations_with_replacement, chain, product

def solution(word):
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    tmp = []
    for i in range(1, 6):
        t = list(product(arr, repeat = i))
        tmp.append(t)
    
    dictionary = []
    for i in list(chain(*tmp)):
        s = ''
        for j in i:
            s += j
        dictionary.append(s)
    
    dictionary.sort()
    answer = dictionary.index(word) + 1
    return answer