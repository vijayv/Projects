#!/usr/bin/python

'''
Exercise 6.5. Write a function named ack
that evaluates Ackermanns function. Use your function to evaluate ack(3, 4), which should be
125. What happens for larger values of m and n? Solution: http: // thinkpython. com/ code/
ackermann. py .
'''

def ack(m,n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m-1, 1)
    if m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))

# print ack(3,4)
# for higher values, max recursion depth is reached

'''
1. Type these functions into a file named palindrome.py and test them out. What happens if
you call middle with a string with two letters? One letter? What about the empty string,
which is written '' and contains no letters?

2. Write a function called is_palindrome that takes a string argument and returns True if it
is a palindrome and False otherwise. Remember that you can use the built-in function len
to check the length of a string.
'''

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):

    word_size = len(word)

    if word_size == 0:
        return True
    if word_size > 0 and (first(word) == last(word)):
        return is_palindrome(middle(word))
    else:
        return False

# print is_palindrome('acaramanamaraca')

'''
Exercise 6.7. A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case.

'''


def is_divisible(a,b):
    return a % b == 0

def is_power_of(x,b):
    return is_divisible(x,b)

def awe_number(a,b):
    return True if is_divisible(a,b) and is_power_of(a/b,b) else False

a = 10
b = 3

# print awe_number(a,b)


'''
Exercise 6.8. The greatest common divisor (GCD) of a and b is the largest number that divides
both of them with no remainder.

One way to find the GCD of two numbers is Euclids algorithm, which is based on the observation
that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can
use gcd(a, 0) = a. Write a function called gcd that takes parameters a and b and returns their greatest common divisor.
'''

def gcd(x,y):
    r = x % y
    return gcd(y,r) if r > 0 else y

print gcd(100,40)

