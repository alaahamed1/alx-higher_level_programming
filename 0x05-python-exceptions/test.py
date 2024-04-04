# try:
#     alist = [1, 2, 3]
#     print(alist[3])
# except IndexError:
#     print("this index is out of the list")
# else:
#     print("unknown error")

# class DogNameError(Exception):
#     def __init__(self, *args, **kwargs):
#         Exception.__init__(self, *args, **kwargs)
        
# try:
#     dogName = input("inter the dog name: ")
#     if any(char.isdigit() for char in dogName):
#         raise DogNameError
# except DogNameError:
#     print("eeeeeerrrrrrror")

num1, num2 = input("Enter an int: ").split()
try:
    res = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, res))
except ZeroDivisionError:
    print("error - 1")
else:
    print("error - 2")
finally:
    print("what's ever ,, ")
