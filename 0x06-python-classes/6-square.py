#!/usr/bin/python3
'''Just class `Square` that defines a square'''


class Square():
    '''class with Private instance attribute: size'''
    pass

    def __init__(self, size=0, position=(0, 0)):
        ''' Instantiation with size optional
        Args:
            size (int): the size of the aquare, must be >= 0'''
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if (isinstance(value, tuple) and
                    len(value) == 2 and
                    value[0] and value[1] >= 0 ):
                self.__position = value
            else:
                raise TypeError
        except Exception:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                if self.__position[0] > 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
