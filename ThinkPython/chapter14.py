#!/usr/bin/python
from os import walk

'''
Exercise 14.1. The os module provides a function called walk that is similar to this one but more
versatile. Read the documentation and use it to print the names of the files in a given directory and
its subdirectories.
Solution: http://www.greenteapress.com/thinkpython/code/walk.py.
'''

def print_dir_contents(directory):
    for entry in walk(directory):
        print entry

'''
Exercise 14.2. Write a function called sed that takes as arguments a pattern string, a replacement
string, and two filenames; it should read the first file and write the contents into the second file
(creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.

If an error occurs while opening, reading, writing or closing files, your program should catch the
exception, print an error message, and exit. Solution: http://www.greenteapress.com/thinkpython/code/sed.py.
'''

def sed(pattern1,pattern2,file1,file2):

    mfile = open(file1)

    ofile = open(file2, 'w')
    for line in mfile:
        if pattern1 in line:
            line = line.replace(pattern1,pattern2)
        ofile.write(line)

    mfile.close()
    ofile.close()

'''
Exercise 14.3. If you download my solution to Exercise 12.4 from http://www.greenteapress.com/thinkpython/code/anagram_sets.py,
youll see that it creates a dictionary that maps from a sorted string of
letters to the list of words that can be spelled with those letters. For example 'opst', maps to the
list ['post','tops','stop','pots'].

Write a module that imports anagram_sets and provides two new functions: store_anagrams
should store the anagram dictionary in a shelf; read_anagrams should look up a word and return
a list of its anagrams. Solution: http://www.greenteapress.com/thinkpython/code/anagram_db.py
'''

def dict_of_anagrams(infile):
    from exercise12 import make_list_of_anagrams

    anagrams = make_list_of_anagrams(infile)

    return anagrams

def store_anagrams(indict):
    import anydbm, pickle

    db = anydbm.open('anagrams.db', 'c')

    for ky, vl in indict.items():
        ky = str(ky)
        vl = pickle.dumps(vl)
        db[ky] = vl

    db.close
    print 'written to db'

def read_anagrams():
    import anydbm, pickle
    db = anydbm.open('anagrams.db')

    for line in db:
        print line

if __name__ == '__main__':

    # exercise 14.1
    # print_dir_contents('C:\\Users\\vvelagapudi\\Documents\\GitHub\\Projects\\ThinkPython')

    # exercise 14.2
    # sed('this','that','sentence.txt','sentence2.txt')

    # for line in open('sentence2.txt'):
    #     print line

    # exercise 14.3W
    splam = dict_of_anagrams('words.txt')
    store_anagrams(splam)
    read_anagrams()


