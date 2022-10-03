#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    # print("Base-10 = {}".format(n))
    l = []
    while n >= 1:
        if n % 2 == 0:
            l.append('0')
            n /= 2
        else:
            l.append('1')
            n = (n - 1) / 2
    l.reverse()
    # print("Base-2 = {}".format("".join(l)))
    item = "".join(l)
    items = item.split('0')
    item_len = [ len(test) for test in items ]
    # print(item_len)
    print(max(item_len))
    # print(math.sqrt(n))
    """
    正確算法： 
    N = 90 > 1011010
    當 90 / 2 = 45...0  商 = 45, 餘 = 0, 第一位數為 0
    當 45 / 2 = 22...1  商 = 22, 餘 = 1, 第二位為 1
    當 22 / 2 = 11...0 商 = 11, 餘 = 0, 第三位為 0
    當 11 / 2 = 5...1 商 = 5, 餘 = 1, 第四位為 1
    當 5 / 2 = 2...1 商 = 2, 餘 = 1, 第五位為 1
    當 2 / 2 = 1...0 商 = 1, 餘 = 0, 第六位為 0
    當 1 / 2 = 0...1 商 = 0, 餘 = 1, 第七位為 1

    1011010 > 2 + 8 + 16 + 64 = 90
    """