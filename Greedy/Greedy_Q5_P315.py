n, m = map(int, input().split())
data = list(map(int, input().split()))

result = 0

# data[0] == data[1] # +1
# data[0] == data[2] # +1
# data[0] == data[3] # +1
# data[0] == data[4] # +1
#
# data[1] == data[2] # +1
# data[1] == data[3] # pass
# data[1] == data[4] # +1

for i in range(len(data)-1):
    for j in range(len(data)-1):
        if i >= j+1:
            pass
        else:

            if data[i] == data[j + 1]:
                pass
            else:
                result += 1

# for i in range(len(data)):
#     if data[i] == data[-1]:
#         pass
#     else:
#         result +=1


print(result)



#답지
array = [0] * 11

for x in data:
    array[x] += 1

result2 = 0

for i in range(1, m + 1):
    n -= array[i]
    result2 += array[i] * n

print(result2)