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

