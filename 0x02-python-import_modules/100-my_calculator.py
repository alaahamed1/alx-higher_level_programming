#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    import sys
    arguments = sys.argv[1:]
    if len(arguments) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = {'+': add, '-': sub, '*': mul, '/': div}
    if sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    res = operator[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))
    print(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), "=", res)
