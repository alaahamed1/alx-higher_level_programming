#!/usr/bin/python3
'''Just class `Square` that defines a square'''


class Square():
    '''class with Private instance attribute: size'''
    pass

    def __init__(self, size=0):
        ''' Instantiation with size optional
        Args:
            size (int): the size of the aquare, must be >= 0'''
        self.__size = size

    @property
    def size(self):
        '''getter method of class Square the size of the aquare,
        must be >= 0 and of course int type'''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Get the area of the square
        Returns: the area of the square'''
        return (self.__size ** 2)

    def my_print(self):
        ''' prints in stdout the square with the character #
        if size is equal to 0, print an empty line'''
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
