#!/usr/bin/python

'''
Exercise 13.1. Write a program that reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.
'''
'''
with open("sentence.txt") as infile:
    import string
    for line in infile:
        for word in line.split(' '):
            word = word.strip()
            for punc in string.punctuation:
                word = word.replace(punc,'')
            print word.lower()
'''
'''
Exercise 13.2. Go to Project Gutenberg (http://www.gutenberg.org/) and download your favorite
out-of-copyright book in plain text format.

Modify your program from the previous exercise to read the book you downloaded, skip over the
header information at the beginning of the file, and process the rest of the words as before.

Then modify the program to count the total number of words in the book, and the number of times
each word is used.

Print the number of different words used in the book. Compare different books by different authors,
written in different eras. Which author uses the most extensive vocabulary?
'''

def process_file(infilename):
    wordlist = []
    with open(infilename) as infile:
        import string
        for line in infile:
            for word in line.split(' '):
                word = word.strip()
                for punc in string.punctuation:
                    word = word.replace(punc,'')
                wordlist.append(word.lower())

        return wordlist


book = {}
def add_to_dict(word):
    global book
    book[word] = book.get(word,0) + 1

mylist = process_file("grim_tales.txt")
mylist.sort()

for entry in mylist:
    add_to_dict(entry)

# print len(book), "different words were used."

'''
Exercise 13.3. Modify the program from the previous exercise to print the 20 most frequently-used
words in the book.
'''

def convert_to_sorted_list(indict):
    outlist = []
    for entry in indict:
        outlist.append((indict[entry],entry))
        outlist.sort(reverse=True)
    return outlist

sortedbookwordslist = convert_to_sorted_list(book)
# print sortedbookwordslist

'''
Exercise 13.4. Modify the previous program to read a word list (see Section 9.1) and then print all
the words in the book that are not in the word list. How many of them are typos? How many of
them are common words that should be in the word list, and how many of them are really obscure?
'''

def compare_to_wordlist(infile):
    with open(infile) as words:
        for word in words:
            if word not in book:
                print word.strip()

# compare_to_wordlist("words.txt")

'''
Exercise 13.5. Write a function named choose_from_hist that takes a histogram as defined in
Section 11.1 and returns a random value from the histogram, chosen with probability in proportion
to frequency.

Your function should return 'a' with probability 2/3 and 'b' with probability 1/3.
'''

sample_hist = {'a':2,'b':1}

def choose_from_hist(hist):
    import random
    val = random.choice(hist.keys())
    print val, "," ,hist[val], "/", sum(hist.values())

# choose_from_hist(sample_hist)

