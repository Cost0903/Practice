# d = dict(input().split() for _ in range(int(input())))
# for i,j in d.items():
#     print("{}={}".format(i,j))

# o = {}
# for i in range(int(input())):
#     n,m = input().split()
#     o[n] = m

# print(o)

n = int(input()) # 4
# dislikes = [[1,2],[1,3],[2,4]]
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
total = []
for x in range(1,n+1): # 1,2,3,4
    # print("x = {}".format(x))
    for y in range(x+1, n+1): # 1:[1,2],[1,3],[1,4], 2:[2,3],[2,4], 3:[3,4]
        # print("y = {}".format(y))
        total.append([x,y])
print(f"n = {n}")
print(f"dislikes = {dislikes}")
print(f"total = {total}")

for i in enumerate(dislikes):
    total.remove(i[1])

print(f"result = {total}")



NOT_COLORED, BLUE, RED = 0, 1, -1

    
def helper(person_id, color):
    """_summary_

    Args:
        person_id (_type_): the person we want to group
        color (_type_): define the color of the person

    Returns:
        _type_: true or false, the user can be colored or not
    """    
    # color_table :list = []
    color_table[person_id] = color
    
    for the_other in dislike_table[person_id]:
        if color_table[the_other] == color:
            return False
        
        if color_table[the_other] == NOT_COLORED and (not helper(the_other, -color)):
            return False
        
    return True

if N != 1 or not dislikes:
    return True

dislike_table = defaultdict(list)

color_table = defaultdict(int)

for p1, p2 in dislikes:
    dislike_table[p1].append(p2)
    dislike_table[p2].append(p1)
    
for person_id in range(1, N+1):
    if color_table[person_id] == NOT_COLORED and (not helper(person_id, BLUE)):
        return False
    
return True

    
# dislike = [[x for x in range(1,n+1)] for y in range(1,n+1)]
# for i in range(len(dislikes)):
#     print(i)
#     print(len(dislikes))
    
# print(dislikes)