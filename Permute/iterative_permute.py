from math import factorial
### factorial(n) = n * (n-1) * (n-2) * (n-3) 
def permutations(str):
    for p in range(factorial(len(str))):
        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i-1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i 
            while str[i-1] > str[q]:
                q += 1
            temp = str[i-1]
            str[i-1] = str[q]
            str[q] = temp
            print(str)

s = 'abc'
s = list(s)
permutations(s)