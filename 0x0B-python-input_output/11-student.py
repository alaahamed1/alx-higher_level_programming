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
        '''retrieves a dictionary representation of a Student instance
        If attrs is a list of strings,only attribute names contained
        in this list must be retrieved.Otherwise,
        all attributes must be retrieved'''
        if attrs is None:
            return self.__dict__
        else:
            my_dict = dict()
            for attr in attrs:
                if attr in self.__dict__:
                    my_dict[attr] = self.__dict__[attr]
            return my_dict

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance:
        You can assume json will always be a dictionary'''
        for key in json:
            if hasattr(self, key):
                setattr(self, key, json[key])
