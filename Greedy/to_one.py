# N -1
# N / k

n, k = map(int, input().split())

result = 0
while n > 1:
    if n % k == 0:
        n = n/k
        result += 1
    else:
        n -= 1
        result += 1

print(result)

"""
n의 범위가 커지면 일일히 1씩 빼는건 어려움 한번에 n이 k배수가 되도록 효율적으로 해야 함
"""
