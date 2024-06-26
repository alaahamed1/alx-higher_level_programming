#!/usr/bin/python3
'''Module of a function def save_to_json_file(my_obj, filename):'''

import json


def save_to_json_file(my_obj, filename):
    ''' function that writes an Object to a text
    file, using a JSON representation:'''
    with open(filename, 'w') as file:
        json_data = json.dumps(my_obj)
        return file.write(json_data)
