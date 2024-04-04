#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        elif isinstance(value, None):
            print(str.format("{:d}"),value)
            return False
    except:
        pass
