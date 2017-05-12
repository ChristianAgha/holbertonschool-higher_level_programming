#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list is []:
        return 0
    score = weight = 0
    for x, y in my_list:
        score += x * y
        weight += y
    return(score / weight)
