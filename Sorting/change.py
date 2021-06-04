n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)


for i in range(k):
    # 작을 때만 해야함 큰 거 바꾸면 안됌
    if a[i] < b[i]:
        a[i] , b[i] = b[i], a[i]
    else:
        break


print(sum(a))