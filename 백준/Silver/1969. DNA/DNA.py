n, m = map(int, input().split())

dna = []
for _ in range(n):
    dna.append(list(input()))

d = []
for i in range(m):
    dict = {}
    for j in range(n):
        if dna[j][i] in dict.keys():
            dict[dna[j][i]] += 1
        else:
            dict[dna[j][i]] = 1

    d.append(dict)


answer = ''
count = 0
for i in d:
    tmp = sorted(i.items(), key = lambda item: [-item[1], item[0]])
    answer += tmp[0][0]
    for j in tmp[1:]:
        count += j[1]

print(answer)
print(count)
