#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    cur_idx = 0
    for i in my_list:
        if idx == cur_idx:
            return i
        cur_idx += 1
