#!/usr/bin/python3
'''Module of a function append_write(filename="", text="")'''


def append_write(filename="", text=""):
    '''append a string at the end of a text file
    (UTF8) and return the number of characters added'''
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
