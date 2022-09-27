# 利用費波那契規則產出 list_len 長度的數列 (list_string 為初始宣告)
def fibonacci(list_string, list_len):
    if (list_len - int(len(list_string))) == 0: 
        return list_string
    else: 
        a = list_string[len(list_string) - 1]
        b = list_string[len(list_string) - 2]
        list_string.append(a + b)
        return fibonacci(list_string, list_len)
        # return fibonacci(list_string.append(list_string[len(list_string) - 1] + list_string[len(list_string) - 2]), list_len)

list_f = [1,1]
print(fibonacci(list_f, 100))
