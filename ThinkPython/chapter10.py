#!/usr/bin/python

'''
Exercise 10.1. Write a function called nested_sum that takes a nested list of integers and add up the elements from all of the nested lists.
'''

def nested_sum(x):
    total = 0
    for each in x:
        for number in each:
            total += number

    return total

y = [[12,40],[12,42]]
# print nested_sum(y)

'''
Exercise 10.2. Use capitalize_all to write a function named capitalize_nested that takes a nested list of strings and returns a new nested list with all strings capitalized.
'''

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(l):
    nex = []
    for s in l:
        nex.append(capitalize_all(s))

    return nex

words = [['trada', 'matt'], ['berkeley', 'unknown']]

# print capitalize_nested(words)

'''
Exercise 10.3. Write a function that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
'''

def cumulative_sum(list):
    new_list = []
    for i in xrange(len(list)):
        new_list.append(sum(list[0:i+1]))

    return new_list

example103 = [1, 2, 3, 4, 5]
# print cumulative_sum(example103)

'''
Exercise 10.4. Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. So middle([1,2,3,4]) should return [2,3].
'''

def middle(list):
    return list[1:len(list)-1]

# print middle(example103)

'''
Exercise 10.5. Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None.
'''

def chop(list):
    list.pop(0)
    list.pop(len(list)-1)

# chop(example103)
# print(example103)

