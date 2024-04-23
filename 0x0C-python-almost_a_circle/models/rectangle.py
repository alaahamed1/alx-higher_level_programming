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
    
    @property
    def width(self):
        '''Getter for width'''
        return self.width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        self.width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        self.height = value

    @property
    def x(self):
        '''Getter for x'''
        return self.x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        self.x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        self.y = value
