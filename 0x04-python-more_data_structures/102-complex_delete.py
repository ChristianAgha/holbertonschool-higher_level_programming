#!/usr/bin/python3
def complex_delete(my_dict, value):

    del_dict = {}

    for k, v in my_dict.items():
        if v == value:
            del_dict[k] = v

    for items in del_dict:
        del my_dict[items]

    return my_dict
