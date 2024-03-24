#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            upper_char = ord(i) - ord('a') + ord('A')
        else:
            upper_char = i
        print("{:c}".format(i))
