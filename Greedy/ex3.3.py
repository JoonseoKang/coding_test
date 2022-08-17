n, m = map(int, input().split())
card = []
card_min = []
for i in range(n):
    in_card = list(map(int, input().split()))
    card.append(in_card)
    card_min.append(min(in_card))




print(max(card_min))