# Enter your code here. Read input from STDIN. Print output to STDOUT
s = int(input())
string = []
for i in range(s):
    string.append(str(input()))

for i in range(len(string)):
    even = ""
    odd = ""
    for j in range(len(string[i])):
        if j == 0:
            even += str(string[i][j])
        elif j % 2 == 0:
            even += str(string[i][j])
        else:
            odd += str(string[i][j])

    print(F'{even} {odd}')