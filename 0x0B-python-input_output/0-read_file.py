#!/usr/bin/python3
'''Module of a function read_file(filename="")'''


def read_file(filename=""):
    '''reads a text file (UTF8) and prints it to stdout'''
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
