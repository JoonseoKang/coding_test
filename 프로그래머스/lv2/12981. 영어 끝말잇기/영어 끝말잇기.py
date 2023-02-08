def solution(n, words):
    history = [words[0]]
    for i in range(1, len(words)):
        if len(words[i])==1:
            return [(i%n)+1, (i+n)//n]
        else:
            if words[i-1][-1] != words[i][0]:
                return [(i%n)+1, (i+n)//n]
            else:
                if words[i] in history:
                    return [(i%n) +1, (i+n) // n]
                else:
                    history.append(words[i])
    
    return [0, 0]