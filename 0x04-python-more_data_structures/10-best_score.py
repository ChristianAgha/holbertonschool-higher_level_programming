#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return("None")
    highest_score = 0
    for k, v in my_dict.items():
        if v > highest_score:
            highest_score = v
            key = k
    return key
