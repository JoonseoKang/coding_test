'''
선택정렬: 가장 작은 것을 골라 맨앞으로 
'''

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    
print(array)

n = int(input())

array = []

for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array.sort(key= lambda x: x[1])

for i in array:
    print(i[0], end=' ')

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))