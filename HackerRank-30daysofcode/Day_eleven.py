#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = [] # [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    
    result = []
    for a in range(len(arr) - 2):
        for b in range(len(arr[a]) - 2):
            a1 = sum(arr[a][b:b+3])
            a2 = arr[(a+1)][b+1]
            a3 = sum(arr[(a+2)][b:b+3])
            result.append(a1+a2+a3)
            
    print(max(result))