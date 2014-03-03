#!/usr/bin/python

''' 
Exercise 3.3. Python provides a built-in function called len that returns the length of a string, so
the value of len('allen') is 5.

Write a function named right_justify that takes a string named s as a parameter and prints the
string with enough leading spaces so that the last letter of the string is in column 70 of the display.

>>> right_justify('allen') 
'''

def right_justify(s):
	offset = 70 - len(s)
	print " " * offset, s

# right_justify('my_text')

'''
Exercise 3.4. A function object is a value you can assign to a variable or pass as an argument. For
example, do_twice is a function that takes a function object as an argument and calls it twice:
def do_twice(f):
f()
f()

Heres an example that uses do_twice to call a function named print_spam twice.
def print_spam():
print 'spam'
do_twice(print_spam)

1. Type this example into a script and test it.
2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
function twice, passing the value as an argument.
3. Write a more general version of print_spam, called print_twice, that takes a string as a
parameter and prints it twice.
4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
argument.
5. Define a new function called do_four that takes a function object and a value and calls the
function four times, passing the value as a parameter. There should be only two statements in
the body of this function, not four.
'''

def do_twice(f,v):
	f(v)
	f(v)

def do_four(f,v):
	do_twice(f,v)
	do_twice(f,v)

def print_spam(intext):
	print intext

# do_four(print_spam,'spam')

'''
1. Write a function that draws a grid like the following:

+ - - - - + - - - - +
| 		  | 		|
| | |
| | |
| | |
+ - - - - + - - - - +
| | |
| | |
| | |
| | |
+ - - - - + - - - - +

Hint: to print more than one value on a line, you can print a comma-separated sequence:
print '+', '-'

If the sequence ends with a comma, Python leaves the line unfinished, so the value printed
next appears on the same line.
print '+',
print '-'
The output of these statements is '+ -'.

A print statement all by itself ends the current line and goes to the next line.

2. Write a function that draws a similar grid with four rows and four columns.

Solution: http: // thinkpython. com/ code/ grid. py 

'''

def print_header(a,b,c):
	line = a + b * 4
	print line * c + a

def print_rows(a,b,c):
	print_header(a,b,c)
	print_header(a,b,c)
	print_header(a,b,c)
	print_header(a,b,c)

print_header("+","-",4)
print_rows("|"," ",4)
print_header("+","-",4)
print_rows("|"," ",4)
print_header("+","-",4)
print_rows("|"," ",4)
print_header("+","-",4)
print_rows("|"," ",4)
print_header("+","-",4)