#!/usr/bin/python3
from calculator_1 import add,div,mul,sub
if __name__ == "__main__":
    a = 10
    b = 5
    add = int("{:d}".format(add(a, b)))
    print(f"{a} + {b} = {add}")
    sub = int("{:d}".format(sub(a, b)))
    print(f"{a} - {b} = {sub}")
    mul = int("{:d}".format(mul(a, b)))
    print(f"{a} * {b} = {mul}")
    div = int("{:d}".format(div(a, b)))
    print(f"{a} / {b} = {div}")
