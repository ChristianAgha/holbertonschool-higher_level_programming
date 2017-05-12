#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for item in list(sorted(my_dict.items())):
        print("{}: {}".format(item[0], item[1]))
