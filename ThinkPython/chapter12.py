#!/usr/bin/python


'''
Exercise 12.1. Many of the built-in functions use variable-length argument tuples. For example,
min()and max() can take any number of arguments:

But sum() does not.

Write a function called sumall() that takes any number of arguments and returns their sum.
'''

def sumall(*args):
    total = 0
    for each in args:
        total += each
    return total

'''
Exercise 12.2. In this example, ties are broken by comparing words, so words with the same length
appear in reverse alphabetical order. For other applications you might want to break ties at random.
Modify this example so that words with the same length appear in random order. Hint:
see the random function in the random module. solution: http://www.greenteapress.com/thinkpython/code/unstable_sort.py
'''

def sort_by_length(words):
    import random
    t = []
    for word in words:
        t.append([len(word), random.random(), word])

    t.sort(reverse=True)

    res = []
    for length, ran, word in t:
        res.append(word)
    return res

if __name__ == '__main__':
    print sumall(1,3,4,5)

    print sort_by_length(['this','that','whom','qualification','quartile','quandary','i','re'])