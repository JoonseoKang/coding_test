def solution(msg):
    answer = []
    dict = {}
    count = 1
    for i in range(65, 91):
        dict[chr(i)] = count
        count += 1
    
    w = ''
    for i in msg:
        w += i
        if w not in dict:
            dict[w] = count
            count += 1
            
            answer.append(dict[w[:-1]])
            w = w[-1]
    
    # final
    answer.append(dict[w])
    return answer