food_times = [3,1,2]
k = 5
answer = 0
n = len(food_times)

for i in range(k+1):
    key = (i % n)

    if food_times[key] != 0:
        food_times[key] -= 1
        answer = key + 1
    else:
        new_key = key + 1
        if new_key >= n:
            new_key = 0
        food_times[new_key] -= 1
        answer = new_key + 1

print(answer)
