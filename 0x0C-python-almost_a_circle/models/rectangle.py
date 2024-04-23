#!/usr/bin/python3
'''Model of the base class'''
from models.base import Base


class Rectangle(Base):
    
    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        '''width of the class Rectangle'''
        return self.width

    @width.setter
    def width(self, value):
        self.width = value

    @property
    def height(self):
        '''height of the class Rectangle'''
        return self.height

    @height.setter
    def height(self, value):
        self.height = value

    @property
    def x(self):
        '''x of the class Rectangle'''
        return self.x

    @x.setter
    def x(self, value):
        self.x = value

    @property
    def y(self):
        '''y of the class Rectangle'''
        return self.y

    @y.setter
    def y(self, value):
        self.y = value
