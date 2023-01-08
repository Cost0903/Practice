def fizzbuzz(n):
    # your code here
    for i in range(n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
    return
# fizzbuzz(15)

def multiply(a, b):
    # your code here
    sum = a
    while abs(b) > 1:
        sum = abs(sum) + abs(a) if (a < 0 and b < 0) or (a > 0 and b > 0) else -abs(sum) - abs(a)
        b = abs(b) - 1
    print(sum)
    return
# multiply(-4, -2)


def prime_numbers(n):
    # your code here
    counter = 0
    num = 2
    # print(len(result))
    while counter != n:
        prime = True
        for i in range(2, num):
            if (i != 1 or i != num) and num % i == 0:
                prime = False
        if prime is True:    
            counter += 1
            print(num)
        num += 1
    return

prime_numbers(7)