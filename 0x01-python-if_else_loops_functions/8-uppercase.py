#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            upper_char = chr(ord(str[i]) - 97 + 65)
        else:
            upper_char = chr(ord(str[i]))
        print("{:s}".format(upper_char), end="")
    print("{:s}".format("\n"), end="")
