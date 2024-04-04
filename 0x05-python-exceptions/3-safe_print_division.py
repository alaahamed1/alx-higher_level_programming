#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print("Inside result:", None)
        return None
    finally:
        if 'res' in locals():
            print("Inside result:{}".format(res))

