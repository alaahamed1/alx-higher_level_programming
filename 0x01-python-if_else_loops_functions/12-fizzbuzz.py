#!/usr/bin/python3
for i in range(1, 101):
    if i % 3 == 0:
        print("{:s}".format("Fizz"), end=" ")
    elif i % 5 == 0:
        print("{:s}".format("Buzz"), end=" ")
    else:
        print("{:d}".format(i), end=" ")
