
# 0x13. JavaScript - Objects, Scopes and Closures project:


Description for all the files and directories in this directory
Any file that does't have a description -if there any- is for testing purposes


`0-rectangle.js` -> an empty class Rectangle that defines a rectangle


`1-rectangle.js` -> a class Rectangle that defines a rectangle:
The constructor must take 2 arguments w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h


`2-rectangle.js` -> same as `1-rectangle.js` and:
If w or h is equal to 0 or not a positive integer, create an empty object


`3-rectangle.js` -> same as `2-rectangle.js` and:
Create an instance method called print() that prints the rectangle using the character X


`4-rectangle.js` -> same as `3-rectangle.js` and:
Create an instance method called rotate() that exchanges the width and the height of the rectangle
Create an instance method called double() that multiples the width and the height of the rectangle by 2


`5-square.js` -> a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
The constructor must take 1 argument: size
The constructor of Rectangle must be called (by using super())


`6-square.js` -> a class Square that defines a square and inherits from Square of 5-square.js:
Create an instance method called charPrint(c) that prints the rectangle using the character c
If c is undefined, use the character X


`7-occurrences.js` -> a function that returns the number of occurrences in a list:
Prototype: exports.nbOccurences = function (list, searchElement)


`8-esrever.js` -> a function that returns the reversed version of a list:
Prototype: exports.esrever = function (list)


`9-logme.js` -> a function that prints the number of arguments already printed and the new argument value. (see example below)

Prototype: exports.logMe = function (item)
Output format: <number arguments already printed>: <current argument value>


`10-converter.js` -> a function that converts a number from base 10 to another base passed as argument:

Prototype: exports.converter = function (base)
