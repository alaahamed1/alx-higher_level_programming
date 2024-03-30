#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    a = 10
    b = 20
    result = int("{:d}".format(add(a, b)))
    print(f"{a} + {b} = {result}")
