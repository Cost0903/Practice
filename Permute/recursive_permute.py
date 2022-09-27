def permute(string, pocket=""):
    # print("pocket =",pocket)
    # print("string =", string)
    if len(string) == 0: print(pocket); print("string =", string)
    else:
        for i in range(len(string)):
            # print("string =", string)
            # print("pocket =",pocket)
            # print("i =", i)
            letter = string[i]
            # print("letter =", letter)
            front = string[0:i]
            # print("front =", front)
            back = string[i+1:]
            # print("back =", back)
            together = front + back
            # print("together =", together)
            permute(together, pocket + letter)

print(permute("ABC", ""))