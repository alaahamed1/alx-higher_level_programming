#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    else:
        new = list(range(len(my_list)))
    new.reverse()
    for i in new:
        print("{:d}".format(my_list[i]))
