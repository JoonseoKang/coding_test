n = int(input())
words = []
for _ in range(n):
    words.append(input())

arr = list(set(words))
arr.sort(key= lambda x: [len(x), x])
for i in arr:
    print(i)