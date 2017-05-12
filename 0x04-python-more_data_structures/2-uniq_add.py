#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    uniq_list = []
    for i in my_list:
        if uniq_list.count(i) == 0:
            uniq_list.append(i)
    for i in uniq_list:
        res += i
    return res
