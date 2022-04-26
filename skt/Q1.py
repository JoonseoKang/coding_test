money = 4578
costs = [1, 4, 99, 35, 50, 1000]
coin = [1, 5, 10, 50, 100, 500]



for i in range(len(costs), 1, -1):
    times = coin[i-1] // coin[i-2]
    # print(times)
    if costs[i-1] >= costs[i-2] * times:
        costs.remove(costs[i-1])
        coin.remove(coin[i-1])



coin.sort(reverse=True)
costs.sort(reverse=True)


how = []
for i in coin:
    how.append(money // i)
    money -= i * (money // i)


result = 0
for i in range(len(costs)):
    result += how[i] * costs[i]

result