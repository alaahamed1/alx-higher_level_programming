#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(int(my_list[i])), end="")
                count += 1
            else:
                continue
    except (ValueError, IndexError):
        pass
    print()
    return count