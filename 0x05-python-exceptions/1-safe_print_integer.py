#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print(value)
            return True
        else:
            return False
    except:
        print()
