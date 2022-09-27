def recur_factorinal(n):
    if n == 1: print(n); return n
    else: print(n);return n * recur_factorinal(n-1)

print(recur_factorinal(5))