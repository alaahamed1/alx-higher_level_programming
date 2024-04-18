#!/usr/bin/python3
'''adds all arguments to a Python list, and then save them to a file
the file named add_item.json
If the file doesn’t exist, it should be created'''


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    item = load_from_json_file("add_item.json")
except Exception:
    item = []
for arg in sys.argv[1:]:
    item.append(arg)
save_to_json_file(item, "add_item.json")
