#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cur_idx = 0
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for i in my_list:
            if cur_idx == idx:
                i = element
                new_list[idx] = element
                return new_list
            cur_idx += 1
