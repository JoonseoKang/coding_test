n, m = map(int, input().split())
card = []

for i in range(n):
    card.append(sorted(list(map(int, input().split()))))

card.sort(key= lambda x: -x[0])
card

print(card[0][0])