#!/bin/python3

# from audioop import reverse
import math
import os
import random
import re
import sys
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    brr = arr.copy()
    brr.reverse()
    sum_a = 0
    sum_b = 0
    # print(reversed(arr))
    for i in range(len(arr)):
        sum_a += arr[i][i]
        sum_b += brr[i][i]
    return abs(sum_a - sum_b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
