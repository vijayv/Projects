#!/usr/bin/python

def test():
    pass

'''
Exercise 11.9. If you did Exercise 10.8, you already have a function named has_duplicates() that
takes a list as a parameter and returns if there is any object that appears more than once in the
list.

Use a dictionary to write a faster, simpler version of . Solution: http://www.greenteapress.com/thinkpython/code/has_duplicates.py
'''

def has_duplicates(t):
    '''
     returns True if any element appears more than once in dict t. Otherwise, returns false.
    '''
    out_dict = {}
    for ele in t:
        try:
            out_dict[ele]
            return True
        except KeyError:
            out_dict[ele] = 1

    return False


# print has_duplicates(["hello","goodbye","hello"])

'''
Exercise 11.10. Two words are rotate pairs if you can rotate one of them and get the other (see
in Exercise 8.12).
Write a program that reads a wordlist and finds all the rotate pairs. Solution: http://www.greenteapress.com/thinkpython/code/rotate_pairs.py
'''
# Incomplete: not working

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

def read_in_dict(file_name):
    out_dict = {}
    with open(file_name) as infile:
        for ent in infile:
            out_dict[ent] = ent

    return out_dict

def find_all_rotated_pairs(indict, n):
    for i in range(1,n):
        for key in indict:
            rotated = rot(key,i)
            if rotated in indict:
                print rotated, i, key

my_dict = read_in_dict("words.txt")

# find_all_rotated_pairs(my_dict,3)

'''
Exercise 11.11 Here’s another Puzzler from Car Talk:

This was sent in by a fellow named Dan O’Leary. He came upon a common one-syllable,
five-letter word recently that has the following unique property. When you remove the
first letter, the remaining letters form a homophone of the original word, that is a word
that sounds exactly the same. Replace the first letter, that is, put it back and remove
the second letter and the result is yet another homophone of the original word. And the
question is, what’s the word?

Now I’m going to give you an example that doesn’t work. Let’s look at the five-letter
word, ‘wrack.’ W-R-A-C-K, you know like to ‘wrack with pain.’ If I remove the first
letter, I am left with a four-letter word, ’R-A-C-K.’ As in, ‘Holy cow, did you see the
rack on that buck! It must have been a nine-pointer!’ It’s a perfect homophone. If you
put the ‘w’ back, and remove the ‘r,’ instead, you’re left with the word, ‘wack,’ which is
a real word, it’s just not a homophone of the other two words.

But there is, however, at least one word that Dan and we know of, which will yield two
homophones if you remove either of the first two letters to make two, new four-letter
words. The question is, what’s the word?

You can use the dictionary from Exercise 11.1 to check whether a string is in the word list.
To check whether two words are homophones, you can use the CMU Pronouncing Dictionary.
You can download it from http://www.speech.cs.cmu.edu/cgi-bin/cmudict or from http://www.greenteapress.com/thinkpython/code/c06d
and you can also download http://www.greenteapress.com/thinkpython/code/pronounce.py, which provides
a function named read_dictionary that reads the pronouncing dictionary and returns a Python dictionary
that maps from each word to a string that describes its primary pronunciation.

Write a program that lists all the words that solve the Puzzler. Solution: http://www.greenteapress.com/thinkpython/code/homophone.py
'''

## Incomplete, this would be good to revisit