def solution(s):
    answer = []
    s = s.replace('{', '')
    tmp = s[:-1].split('}')
    tu = []
    for i in tmp:
        
        r = i.replace(',', ' ')
        r = r.lstrip()
        arr = list(map(int, r.split()))
        if arr:
            tu.append(arr)
    
    tu.sort(key = lambda x: len(x))
    
    for i in sum(tu, []):
        if i not in answer:
            answer.append(i)
    

        


    return answer