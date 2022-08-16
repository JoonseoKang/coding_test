```
500원, 100원, 50원, 10원 무한히 존재
거스름돈 N원일때 동전의 최소 개수
```

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += 1
    n &= coin

print(count)
