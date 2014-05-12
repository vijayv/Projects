#!/usr/bin/python

'''
Exercise 6.1. Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.
'''

def compare(x,y):
    return 1 if x > y else 0

'''
Exercise 6.2. Use incremental development to write a function called hypotenuse that returns the
length of the hypotenuse of a right triangle given the lengths of the two legs as arguments. Record
each stage of the development process as you go.
'''

def hypotenuse(x,y):
    '''
     Returns the length of the hypotenuse given the length of the two legs
    '''
    from math import sqrt
    square = x**2 + y**2
    print sqrt(square)


'''
Exercise 6.3. Write a function is_between(x, y, z) that returns True if x <= y <= z or False
otherwise.
'''

def is_between(x,y,z):
    return x <= y <= z


'''
Recursion Stuff
'''

def factorial(n):
    if not isinstance(n,int):
        print "factorial is only defined for integers"
        return None
    elif n < 0:
        print "factorial is only defined for positive integers"
        return None
    elif n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

# Fibonacci

def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    hypotenuse(3,4)
    print "is_between is", is_between(1,2,3)
    print "factorial is", factorial(3)
    print "fibonacci is", fibonacci(8)