def score(total, correct, wrong):
    # your code here
    return (correct * 2 + wrong) / (total * 2) * 100


print(f"Your score is {score(20, 0, 20)}.")