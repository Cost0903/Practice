def score75(total, correct, wrong):
    # your code here
    print(f"total = {total}, currect = {correct}, wrong = {wrong}, pick 75%")
    print(f"total * 0.75 = {total * 0.75}")
    print((30*0.75 + 10*0.75)/(40*0.75))
    print(max(total*.75, correct))
    return (min(total * .75 * 2, correct * 2) + min(total * .75 - min(total * .75, correct), wrong)) / (total * .75 * 2) * 100


print(f"Your score is {score75(20, 0, 20)}.")