n = 5
start_time = [1, 3, 3, 5 ,7]
running_time = [2, 2, 1, 2, 1]

t = []

for i in range(n-1):
    time = start_time[i+1] - start_time[i]
    t.append(time)

start_time[-2] + running_time[-2] <= start_time[-1] # +1

for i in range(n-1):
    if t[i] >= running_time[i]:
        print(start_time[i])


running_time[:-1]
t
start_time
end_time

start_time
sorted(end_time)

set(start_time)

count = 1
for i in range(n-1):
    if end_time[i] <= start_time[i+1]:
        count += 1

