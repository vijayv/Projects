#!/usr/bin/python

'''
Exercise 12.3. Write a function called most_frequent that takes a string and prints the letters
in decreasing order of frequency. Find text samples from several different languages and see
how letter frequency varies between languages. Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies.
Solution:
'''

def most_frequent(word):
    freq = {}
    for letter in word:
        try:
            freq[letter] += 1
        except KeyError:
            freq[letter] = 1

    sort_freq = []
    for entry in freq:
        sort_freq.append((freq[entry], entry))

    sort_freq.sort(reverse=True)

    for num, let in sort_freq:
        print let, "-", num

# most_frequent('qualifications')

'''
12.4 More Anagrams!

Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
words that are anagrams.
Here is an example of what the output might look like:

['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']

Hint: you might want to build a dictionary that maps from a set of letters to a list of words
that can be spelled with those letters. The question is, how can you represent the set of letters
in a way that can be used as a key? -- Use a tuple!

'''

anagram_dict = {}

def make_into_key(word):
    lst = list(word)
    lst.sort()

    tpl = tuple(lst)
    return tpl

def add_to_dict(anag, word):
    global anagram_dict
    try:
        anagram_dict[anag].append(word)
    except KeyError:
        anagram_dict[anag] = [word]

def make_list_of_anagrams(infile):
    with open(infile) as wordlist:
        for word in wordlist:
            mykey = make_into_key(word.strip())
            add_to_dict(mykey,word.strip())

make_list_of_anagrams("words.txt")
# for k in anagram_dict:
#     if len(anagram_dict[k]) > 1:
#         print k, anagram_dict[k]

'''
12.4 2. Modify the previous program so that it prints the largest set of anagrams first, followed by the
second largest set, and so on.
'''

# sorted_anagrams = []
# for k in anagram_dict:
#     if len(anagram_dict[k]) > 1:
#         sorted_anagrams.append((len((anagram_dict[k])), k, anagram_dict[k]))
#
# sorted_anagrams.sort(reverse=True)
# for cnt, ang, wrds in sorted_anagrams:
#     print ang, wrds

'''
Exercise 12.5. Two words form a metathesis pair if you can transform one into the other by
swapping two letters; for example, converse and conserve. Write a program that finds all of
the metathesis pairs in the dictionary. Hint: dont test all pairs of words, and dont test all possible
swaps. Solution: http://www.greenteapress.com/thinkpython/code/metathesis.py.
'''

only_anagrams = []
for k in anagram_dict:
    if len(anagram_dict[k]) > 1:
        only_anagrams.append(anagram_dict[k])

for each in only_anagrams:
    for idx in range(0,len(each)):
        if len(each[idx]) == len(each[idx-1])
            for idxl in range(0,len(each[idx])):
                repeats = 0
                if repeats > 1:
                    break
                elif letter == element:
                    pass
                else:
                    repeats += 1
            print each[idx], each[idx-1]

