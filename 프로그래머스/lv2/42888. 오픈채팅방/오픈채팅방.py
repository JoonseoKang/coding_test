def solution(record):
    answer = []
    dict = {}
    tmp = []
    for i in record:
        
        state, user_id = i.split()[0], i.split()[1]
        try:
            if i.split()[2]:
                dict[user_id] = i.split()[2]
        except:
            pass
        
        if state == 'Enter':
            tmp.append([user_id , '님이 들어왔습니다.'])
        if state == 'Leave':
            tmp.append([user_id , '님이 나갔습니다.'])
        
    
    for idx , i in enumerate(tmp):
        answer.append(dict[i[0]] + i[1])
        
        
    return answer