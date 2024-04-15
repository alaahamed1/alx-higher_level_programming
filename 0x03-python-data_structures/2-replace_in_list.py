#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    new_list = my_list[:]
    cur_idx = 0
    for i in my_list:
        if idx == cur_idx:
            i = element
            new_list[idx] = element
            return new_list
        cur_idx += 1
