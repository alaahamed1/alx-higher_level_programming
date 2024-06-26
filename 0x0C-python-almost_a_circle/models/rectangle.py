#!/usr/bin/python3
'''Model of the base class'''
from models.base import Base


class Rectangle(Base):
    '''class Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __validation(self, name, value, q=True):
        '''Raise Error if value not a positive int'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 and q:
            raise ValueError("{} must be >= 0".format(name))
        if value <= 0 and not q:
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        '''Getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        self.__validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        self.__validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''Getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        self.__validation("x", value)
        self.__x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        self.__validation("y", value)
        self.__y = value
