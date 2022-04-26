from itertools import combinations

mmr = [33,56,93,31,18,10,41,93]
m = [33,33,5,1,2]
t = list(combinations(mmr, 4))

score = []
for i in t:
    score.append(sum(list(i)))

score = list(set(score))
score.sort()

len(score)/2

score[21]
score[20]
