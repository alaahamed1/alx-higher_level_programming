#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            upper_char = ord(i) - 97 + 65
            print(chr(upper_char), end='')
        else:
            print(i, end='')
