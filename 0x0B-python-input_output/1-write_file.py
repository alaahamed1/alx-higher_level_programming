#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, encoding="utf-8") as file:
        file.write(text)
