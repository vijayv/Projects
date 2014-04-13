#!/usr/bin/python

'''
Exercise 10.6. Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that the elements of the list can be compared with the relational operators <, >, etc.
'''

def is_sorted(t):
    return True if t == t.sorted() else False

example = [1,2,4,5,12,6,3]

print is_sorted(example)