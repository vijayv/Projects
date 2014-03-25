'''
Exercise 8.1. Write a function that takes a string as an argument and displays the letters backward,
one per line.
'''

def print_reverse(x):
    for each in range(0,len(x)):
        print x[-(each+1)]

# print_reverse("This is a long sentence!")

'''
Exercise 8.2. Modify the program to fix this error.
'''

def duck_names():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        print letter + suffix if letter <> 'O' and letter <> 'Q' else letter + 'uack'

# duck_names()

'''
Exercise 8.3. Given that fruit is a string, what does fruit[:] mean?

Answer: It returns the entire string: index the string from beginning to end.
'''

'''
Exercise 8.4. Modify find so that it has a third parameter, the index in word where it should start
looking.
'''

def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

# print find("thiasjdfajskdfha","s",3)


'''
Exercise 8.5. Encapsulate this code in a function named count, and generalize it so that it accepts
the string and the letter as arguments.
'''

def counter(word, lkup):
    count = 0
    for letter in word:
        if letter == lkup:
            count = count + 1
    print count

# counter("ssssthis","s")

'''
Exercise 8.6. Rewrite this function so that instead of traversing the string, it uses the threeparameter
version of find from the previous section.
'''

def counter2(word, lkup):
    count = 0
    search = 0
    while find(word,lkup,search) > -1:
        search = find(word,lkup,search) + 1
        count = count + 1
    print count

# counter2("This is a super long sentence isn't it?","n")

'''
Exercise 8.7. There is a string method called count that is similar to the function in the previous
exercise. Read the documentation of this method and write an invocation that counts the number of
as in 'banana'.
'''

# print 'banana'.count('a')

'''
Exercise 8.8. Read the documentation of the string methods at http: // docs. python. org/ 2/
library/ stdtypes. html# string-methods . You might want to experiment with some of them
to make sure you understand how they work. strip and replace are particularly useful.

The documentation uses a syntax that might be confusing. For example, in
find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but
start is optional, and if you include start, then end is optional.
'''

# print '  empty space   '
# print '  empty space   '.strip()
#
# print 'empty space'.replace("s","c")

'''
Exercise 8.9. Starting with this diagram, execute the program on paper, changing the values of i
and j during each iteration. Find and fix the second error in this function.

Answer: The reason that it only runs 3 times is because of the "> 0", it should be changed to ">= 0"
'''