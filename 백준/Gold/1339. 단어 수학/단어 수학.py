word = []
n = int(input())
for _ in range(n):
    word.append(input())

dict = {}
for w in word:
    square_root = len(w) - 1
    for c in w:
        if c in dict:
            dict[c] += pow(10, square_root)
        else:
            dict[c] = pow(10, square_root)
        square_root -= 1

dict = sorted(dict.values(), reverse=True)
result, m = 0, 9

for value in dict:
    result += value * m
    m -= 1

print(result)
