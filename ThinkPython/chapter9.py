#!/usr/bin/python

'''
Exercise 9.1. Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace).
'''
with open("words.txt") as infi:
    for line in infi:
        if len(line.strip()) > 20:
            pass
            # print line.strip()

'''
Exercise 9.2. In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter e. Since e is the most common letter in English, thats not easy to do.
In fact, it is difficult to construct a solitary thought without using that most common symbol. It is slow going at first, but with caution and hours of training you can gradually gain facility.
All right, Ill stop now.

Write a function called has_no_e that returns True if the given word doesnt have the letter e in it.
Modify your program from the previous section to print only the words that have no e and compute the percentage of the words in the list have no e.
'''


def has_no_e(word):
    return True if 'e' not in word else False

def percent_of_e(list):
    count = 0.0
    for word in list:
        if has_no_e(word):
            count += 1

    return (count / len(list)) * 100


'''
Exercise 9.3. Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if the word doesnt use any of the forbidden letters.
Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that dont contain any of them.
Can you find a combination of 5 forbidden letters that excludes the smallest number of words?
'''

def has_letter(word, letter):
    return True if letter in word else False

def has_forbidden_letters(word_list):
    letter_list = []
    u_in = ""
    while u_in <> "done":
        u_in = raw_input("add forbidden letter: \n\r").lower()
        letter_list.append(u_in)

    allowed = 0

    for word in word_list:
        for letter in letter_list:
            if not has_letter(word, letter):
                allowed += 1

    list_length = len(word_list)
    print "Out of", list_length, ", ", allowed, "are allowed."


# def count_of_acceptable_words(word_list):

if __name__ == '__main__':
    print has_no_e("som")
    word_list = ["asd", "erewe", "asdfas", "asdfk"]

    print percent_of_e(word_list), "% have no e..."

    has_forbidden_letters(word_list)
