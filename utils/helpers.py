import random

def weighted_choice(choices: dict):
    total = sum(choices.values())
    r = random.uniform(0, total)
    upto = 0
    for k, v in choices.items():
        if upto + v >= r:
            return k
        upto += v
