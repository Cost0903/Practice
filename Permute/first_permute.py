from math import factorial

def permute(str):
    ## 首先要先計算幾次後結束 使用 factorial 計算
    for i in range(factorial(len(str))):
        # 比照之前的做法，先將第一個字元取出，後兩個字元去排序
        print(''.join(str))

    return



# s = 'abc'
# s = list(s)
s = ['a','b','c']
permute(s)


# for i in range(len(s)):
#     letter = s[i]
#     front = s[0:i]
#     back = s[i+1:]
#     print(letter)#####3
#     print(front)
#     print(back)