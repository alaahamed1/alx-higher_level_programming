#!/usr/bin/python3
import sys
if __name__ == "__main__":
    script_name = sys.argv[0]
arguments = sys.argv[1:]
if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print(f"{len(sys.argv) - 1}", "argument:")
    for index in (sys.argv[1:]):
        print(f"{len(sys.argv) - 1}:", sys.argv[1])
else:
    print(f"{len(sys.argv) - 1} arguments:")
    for index, arg in enumerate(arguments, 1):
        print(f"{index}: {arg}")
