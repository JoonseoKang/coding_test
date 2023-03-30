from itertools import product

num = [1, 2, 3]


for _ in range(int(input())):
    n = int(input())
    answer = 0
    for i in range(1, n+1):
        for c in product(num, repeat=i):
            if sum(c) == n:
                answer += 1

    print(answer)
