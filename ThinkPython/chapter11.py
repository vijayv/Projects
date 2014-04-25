#!/usr/bin/python

'''
Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a dictionary.
It doesnt matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
'''

def dict_value(s_word, indict):
    return indict.get(s_word)

def dict_search(s_word, indict):
    return s_word in indict

def make_dict(infile):
    out_dict = {}
    for word in infile:
        out_dict[word.strip()] = 1

    return out_dict

my_file = open('words.txt')
my_dict = make_dict(my_file)

# print dict_search('overgrown', my_dict)

'''
Exercise 11.2. Dictionaries have a method called get that takes a key and a default value.
If the key appears in the dictionary, get returns the corresponding value; otherwise it returns the default value.
'''

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1

    return d

# print histogram('callous')

'''
Exercise 11.3. Dictionaries have a method called keys that returns the keys of the dictionary, in no particular order, as a list.
Modify print_hist to print the keys and their values in alphabetical order.
'''

def sorted_dict(l):
    list = l.keys()
    list.sort()

    for entry in list:
        print entry, l.get(entry)

# sorted_dict(my_dict)

'''
Exercise 11.4. Modify reverse_search so that it builds and returns a list of all keys that map to v or an empty list if there are none.
'''

def reverse_lookup(d,v):
    lkup = []
    for k in d:
        if d[k] == v:
            lkup.append(k)
    return lkup

h = histogram("parrot")
k = reverse_lookup(h,2)
# print k

'''
Exercise 11.5. Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict.
'''
# INCOMPLETE
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        dict.setdefault(val, [key])
        else:
            inverse[val].append(key)
    return inverse


