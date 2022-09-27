# 利用費波那契規則產出 list_len 長度的數列 (list_string 為初始宣告)
def fibonacci(list_string, list_len):
    for i in range(2,list_len):
        list_string.append(list_string[i-2] + list_string[i-1])
    return list_string

list_f = [1,1]
print(fibonacci(list_f, 100))
