#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solution' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. 2D_STRING_ARRAY items
#  2. INTEGER orderBy
#  3. INTEGER orderDirection
#  4. INTEGER pageSize
#  5. INTEGER pageNumber
#
##############
items_rows = int(input().strip())
items_columns = int(input().strip())

items = []

for _ in range(items_rows):
    items.append(input().rstrip().split())

orderBy = int(input().strip())

orderDirection = int(input().strip())

pageSize = int(input().strip())

pageNumber = int(input().strip())
##############
def solution(items, orderBy, orderDirection, pageSize, pageNumber):
    tmp = sorted(items, key=lambda i: i[orderBy], reverse=orderDirection)
    # len(items) = n

    if len(items) < pageNumber:
        for i in tmp:
            print(i[0])
    else:
        if ((pageNumer + 1) * pageSize) > len(items):
            for i in range(len(items) % pageSize):
                print(tmp[i - (len(items) % pageSize)][0])
        else:
            for j in range(pageSize):
                print(tmp[(pageSize * pageNumber) + i][0])

result = solution(items, orderBy, orderDirection, pageSize, pageNumber)

len(items)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    items_rows = int(input().strip())
    items_columns = int(input().strip())

    items = []

    for _ in range(items_rows):
        items.append(input().rstrip().split())

    orderBy = int(input().strip())

    orderDirection = int(input().strip())

    pageSize = int(input().strip())

    pageNumber = int(input().strip())

    result = solution(items, orderBy, orderDirection, pageSize, pageNumber)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
