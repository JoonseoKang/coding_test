n, m = map(int, input().split())

poketmon = []
for i in range(n):
    poketmon.append(input())

poketmon_dict = {p: i+1 for i, p in enumerate(poketmon)}

for i in range(m):
    quiz = input()
    print(poketmon_dict[quiz] if quiz in poketmon_dict else poketmon[int(quiz) - 1])
