#!/usr/bin/python

'''
Exercise 10.6. Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that the elements of the list can be compared with the relational operators <, >, etc.
'''

def is_sorted(t):
    return True if t == sorted(t) else False

example = [1,2,4,5,12,6,3]
sorted_example = sorted(example)

# print is_sorted(sorted_example)

'''
Exercise 10.7. Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
'''

def is_anagram(word_one, word_two):
    for letter in word_one:
        if letter not in word_two:
            return False

    return True

# print is_anagram('trada', 'artad')
# print is_anagram('trada', 'harada')

'''
Exercise 10.8. The (so-called) Birthday Paradox:
1. Write a function called has_duplicates that takes a list and returns True if there is any
element that appears more than once. It should not modify the original list.
2. If there are 23 students in your class, what are the chances that two of you have the same
birthday? You can estimate this probability by generating random samples of 23 birthdays and
checking for matches. Hint: you can generate random birthdays with the randint function
in the random module.
'''

def has_duplicates(t, word):
    '''
     returns True is word exists in list t. Otherwise, return false.
    '''
    if t.count(word) > 1:
        return True
    return False

def gen_n_birthdays(n):
    import random
    bdays = []
    for i in range(n):
        bdays.append(random.randint(1,365))

    return bdays

def percent_of_dupes(t):
    dupes = 0.0
    for entry in t:
        if has_duplicates(t, entry):
            dupes += 1
    return dupes / len(t)

example_bdays = gen_n_birthdays(23)
# print percent_of_dupes(example_bdays)

'''
Exercise 10.9. Write a function called remove_duplicates that takes a list and returns a new
list with only the unique elements from the original. Hint: they dont have to be in the same order.
'''

def remove_duplicates(t):
    '''
     returns a new list with only unique values from list t.
    '''
    for entry in t:
        if has_duplicates(t, entry):
            del t[t.index(entry)]
    return t

cities = ['Denver', 'San Francisco', 'Los Angeles', 'Boston', 'Denver', 'San Francisco']
print remove_duplicates(cities)
print cities
