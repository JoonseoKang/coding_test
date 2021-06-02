n = int(input())

result = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in list(str(i)) or '3' in list(str(j)) or '3' in list(str(k)):
                result += 1

print(result)

