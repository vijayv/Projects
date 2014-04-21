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
# print remove_duplicates(cities)
# print cities

'''
Exercise 10.10. Write a function that reads the file words.txt and builds a list with one element per word.
Write two versions of this function, one using the append method and the other using the idiom t = t + [x].
Which one takes longer to run? Why?
'''

def make_list(infile):
    mylist = []
    with open(infile) as ppp:
        for word in ppp:
            mylist.append(word.strip())

    return mylist

def make_list2(infile):
    mylist = []
    with open(infile) as ppp:
        for word in ppp:
            mylist = mylist + [word]

    return mylist

# print make_list2('words.txt')

# Method 1 takes much less time to run

'''
10.11 Bisect, search for word
'''

def bisect_find(s_word, inlist):
    '''
     Takes a string and list. Returns the string if it exists in the list, otherwise it will return None.
    '''

    halfway = len(inlist) // 2
    list_length = len(inlist)

    top_half = inlist[0 : halfway]
    bottom_half = inlist[halfway : list_length + 1]

    if list_length <= 1:
        return inlist
    elif s_word in top_half:
        bisect_find(s_word, top_half)
    elif s_word in bottom_half:
        bisect_find(s_word, bottom_half)
    else:
        return None

inlist = make_list('words.txt')
# print bisect_find('overbore', inlist)

def bisect(s_word, inlist):
    '''
     Find the index of the given word in the the given list.
    '''

    halfway = len(inlist) // 2
    list_length = len(inlist)

    top_half = inlist[0 : halfway]
    bottom_half = inlist[halfway : list_length]

    print top_half

    if s_word in top_half:
        print "looking for", s_word, "in the top half"
        top_half.index(s_word)
    elif s_word in bottom_half:
        print "looking for", s_word, "in the bottom half"
        bottom_half.index(s_word)
    else:
        return None

# This is not working for some reason?
# print bisect('aah', inlist)

'''
Exercise 10.12. Two words are a reverse pair if each is the reverse of the other.
Write a program that finds all the reverse pairs in the word list.
'''

def reverse_word(in_word):
    return in_word[::-1]

def all_reverse(inlist):
    reverse_list = []
    for each in inlist:
        # if reverse_word(each) in inlist:
        #     reverse_list.append(each)
        if bisect_find(reverse_word(each), inlist):
            reverse_list.append(each)

    return reverse_list

# print all_reverse(inlist)

'''
Exercise 10.13. Two words interlock if taking alternating letters from each forms a new word.
For example, shoe and cold interlock to form schooled.
1. Write a program that finds all pairs of words that interlock. Hint: dont enumerate all pairs!
2. Can you find any words that are three-way interlocked; that is, every third letter forms a word, starting from the first, second or third?
'''

def is_interlocked(x,y,inlist):
    concat_word = x + y
    for word in inlist:
        return is_anagram(concat_word, word)

def find_all_interlocked_pairs(x, y, inlist):
    interlocked_pairs = []

    for word in inlist:
        if is_interlocked(x, y, inlist):
            interlocked_pairs.append(word)

    return interlocked_pairs

print is_interlocked('aa', 'b', inlist)
print find_all_interlocked_pairs('ab', 'a', inlist)