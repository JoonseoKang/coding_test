from collections import deque

prices = [1,2,3,2,3]

prices = deque(prices)

answer = []

while (prices):
    num = prices.popleft()
    count = 0
    for i in prices:
        if num <= i:
            count += 1
        else:
            break
    answer.append(count)


print(answer)