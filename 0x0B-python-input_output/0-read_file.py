#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        '''reads a text file (UTF8) and prints it to stdout'''
        for line in file:
            print(line, end='')
