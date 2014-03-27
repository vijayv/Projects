#!/usr/bin/python

'''
Exercise 8.10. A string slice can take a third index that specifies the step size; that is, the number
of spaces between successive characters. A step size of 2 means every other character; 3 means every
third, etc.
'''

def is_palindrome(word):
    # word[::01] prints the word in reverse
    if word == word[::-1]:
        return True
    else:
        return False

'''
Exercise 8.11. The following functions are all intended to check whether a string contains any
lowercase letters, but at least some of them are wrong. For each function, describe what the function
actually does (assuming that the parameter is a string).
'''


# This works as intended
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

# this returns stings rather than a boolean value
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# this works as intended
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# this always returns false
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# This works as intended
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

'''
Exercise 8.12. ROT13 is a weak form of encryption that involves rotating each letter in a word
by 13 places. To rotate a letter means to shift it through the alphabet, wrapping around to the
beginning if necessary, so A shifted by 3 is D and Z shifted by 1 is A.

Write a function called rotate_word that takes a string and an integer as parameters, and that
returns a new string that contains the letters from the original string rotated by the given amount.
For example, cheer rotated by 7 is jolly and melon rotated by -10 is cubed.

You might want to use the built-in functions ord, which converts a character to a numeric code,
and chr, which converts numeric codes to characters.

Potentially offensive jokes on the Internet are sometimes encoded in ROT13. If you are not easily
offended, find and decode some of them.
'''

def rotate_letter(x,n):
    import string
    letters = string.lowercase
    index = (letters.find(x) + n) % len(letters)
    return letters[index]

def rot(word, n):
    rot_word = ''
    for letter in word:
        rot_word = rot_word + rotate_letter(letter,n)
    print rot_word

# rot('melon',-10)