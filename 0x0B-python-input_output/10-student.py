#!/usr/bin/python3
'''Module of only one class Student'''


class Student:
    '''Defines a student by:
    Public instance attributes:
        first_name, last_name, age
    '''
    def __init__(self, first_name, last_name, age):
        '''Instantiation with first_name, last_name and age'''
        self.first_name = first_name,
        self.last_name = last_name,
        self.age = age
        
    def to_json(self, attrs=None):
        
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
