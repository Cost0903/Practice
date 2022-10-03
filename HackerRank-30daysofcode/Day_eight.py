lines = int(input())
result = {}
for i in range(lines):
    try:
        data = input().split(' ')
        result[data[0]] = data[1]
    except:
        continue
    
# Hint: the try/except 
# Because the query lines is unknown number
# When the last of query, it will shows EOFError Exception
# So, the try/except will end this for loop
while True:
    try:
        query = input()
    except:
        break
    if result.get(query):
        print("{}={}".format(query, result[query]))
    else:
        print("Not found")