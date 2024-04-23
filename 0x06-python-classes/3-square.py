#!/usr/bin/python3
'''Just class `Square` that defines a square'''


class Square:
    '''class with Private instance attribute: size'''
    pass

    def __init__(self, size=0):
        '''Instantiation with size optional
        Args:
            size (int): the size of the aquare, must be >= 0'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
