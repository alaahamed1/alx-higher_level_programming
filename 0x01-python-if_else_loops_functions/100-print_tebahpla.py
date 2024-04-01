#!/usr/bin/python3
for char in range(122, 96, -1):
    res = char
    if char % 2 != 0:
        res -= (ord('a') - ord('A'))
    print("{:s}".format(chr(res)), end="")
