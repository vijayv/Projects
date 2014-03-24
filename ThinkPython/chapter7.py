#/usr/bin/python
'''
Exercise 7.1. Rewrite the function print_n from Section 5.8 using iteration instead of recursion.
'''

def print_n(x,y):
    while y > 0:
        print x
        y = y-1
    return

# print_n("hello",15)

'''
Exercise 7.2. Encapsulate this loop in a function called square_root that takes a as a parameter,
chooses a reasonable value of x, and returns an estimate of the square root of a.
'''

def square_root(a):
    epsilon = .0000001
    x, y = 1, 0
    while abs(y-x) > epsilon:
        x = a/2
        y = (x + a/x) / 2

    return x, "is the square root"

# doesn't work!
# print square_root(16)
