#!/usr/bin/python3
def pascal_triangle(n):
    '''This function generates a list of lists
    representing Pascal's Triangle up to level n'''
    if n <= 0:
        return []
    pascal_list = []
    for i in range(n):
        row = [1]
        pascal_list.append(row)
        if i > 0:
            for j in range(0, i):
                element = pascal_list[i - 1][j - 1] + pascal_list[i - 1][j]
                row.append(element)
            row.append(1)
    return pascal_list
