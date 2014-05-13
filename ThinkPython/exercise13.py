#!/usr/bin/python

from chapter11 import histogram
from chapter13 import process_file, convert_to_sorted_list

'''
Exercise 13.9. The rank of a word is its position in a list of words sorted by frequency: the most
common word has rank 1, the second most common has rank 2, etc.
Zipfs law describes a relationship between the ranks and frequencies of words in natural languages
(http://en.wikipedia.org/wiki/Zipfs_law). Specifically, it predicts that the frequency,
f , of the word with rank r is:

f = cr^-s

where s and c are parameters that depend on the language and the text. If you take the logarithm of
both sides of this equation, you get:

log f = log c - s log r

So if you plot log f versus log r, you should get a straight line with slope -s and intercept log c.
Write a program that reads a text from a file, counts word frequencies, and prints one line for each
word, in descending order of frequency, with log f and log r. Use the graphing program of your
choice to plot the results and check whether they form a straight line. Can you estimate the value of
s?
Solution: http://www.greenteapress.com/thinkpython/code/zipf.py. To make the plots, you might have to
install matplotlib (see http://matplotlib.org/).
'''

if __name__ == '__main__':
    print "Exercise 13:"

    mylist = process_file('emma.txt')
    myhist = histogram(mylist)
    sorted_list = convert_to_sorted_list(myhist)

    freq_list = []
    for freq in sorted_list:
        freq_list.append(freq[0])

    for idx, freq in enumerate(freq_list):
        print idx, freq
