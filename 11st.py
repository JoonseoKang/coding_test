a = [ 6,1,4,6,3,2,7,4]
a[3:5]
a[4:6]

k = 3
l = 2
tmp = []
for i in range(len(a)):
    b = a[i:i+k]
    if len(b) == k:
        for j in range(len(a)):
            if (j+l <= i or j  >= i+k) :
                c = a[j:j+l]
                if len(c) == l:
                    tmp.append(sum(b) + sum(c))

max(tmp)


def solution(A, K, L):
    # write your code in Python 3.6
    tmp = []
    if len(A) < K + L:
        return -1
    else:
        for i in range(len(A)):
            b = A[i:i + K]
            if len(b) == K:
                for j in range(len(A)):
                    if j + L <= i or j >= i + K:
                        c = A[j:j + L]
                        if len(c) == L:
                            tmp.append(sum(b) + sum(c))

        return max(tmp)