meeting = []
for _ in range(int(input())):
    meeting.append(list(map(int, input().split())))

meeting.sort(key= lambda x: [x[1], x[0]])

start_time, end_time = 0, 0
answer = 0
for i in meeting:
    new_start, new_end = i[0], i[1]
    if new_start >= end_time:
        answer += 1
        start_time = new_start
        end_time = new_end

print(answer)
        
        