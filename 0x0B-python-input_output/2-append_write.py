#!/usr/bin/python3
'''Module of a function append_write(filename="", text="")'''


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as file:
        '''Write a function that appends a string at the end of
        a text file (UTF8) and returns the number of characters added'''
        return file.write(text)
