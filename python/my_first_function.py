import random

foregrounds = ["\033[90m", "\033[91m", "\033[93m", "\033[94m"]
adornments = "@*&$"

def dress_tree(cnt: int):
    for _ in range(cnt):
        adornment_idx = random.randint(-1, len(adornments) - 1)
        color_idx = random.randint(0, len(foregrounds) - 1)
        if adornment_idx == -1:
            print("\033[0m#", end="")
        else:
            print(foregrounds[color_idx], end="")
            print(adornments[adornment_idx], end="")
    print("\033[0m", end="")

dress_tree(10)
