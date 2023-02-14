def solution(n, left, right):
    tmp = []
    num = 0
    for i in range(left - left%n, n**2):
        if i > right:
            break
            
        if i//n == 0:
            tmp.append(i+1)

        elif i//n == n-1:
            tmp.append(n)

        else:
            num = max(num, (i // n) + 1)
            if i%n > i // n:
                num += 1
                tmp.append(num)
            else:
                num = (i // n) + 1
                tmp.append(num)

    return tmp[left%n:]