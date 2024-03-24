#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            upper_char = ord(i) - 97 + 65
        else:
            upper_char = i
    print("{:d}".format(i))
