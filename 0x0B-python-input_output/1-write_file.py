#!/usr/bin/python3
'''Module of a function write_file(filename="", text="")'''


def write_file(filename="", text=""):
    '''writes a string to a text file (UTF8) and
    returns the number of characters written'''
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
