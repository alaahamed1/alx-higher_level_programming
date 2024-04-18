#!/usr/bin/python3
'''Module of a function def to_json_string(my_obj):'''

import json


def to_json_string(my_obj):
    ''' a function that returns the JSON
    representation of an object (string)'''
    json_data = json.dumps(my_obj)
    return json_data
