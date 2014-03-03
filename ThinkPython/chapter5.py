#!/usr/bin/python

def countdown(n):
	if n <= 0:
		print 'Blastoff!'
	else:
		print n
		countdown(n-1)

# countdown(3)

def print_n(s, n):
	if n <= 0:
		return
	print s
	print_n(s, n-1)

# exercise 5.1
def do_n(f, n):
	''' Return function "f" "n" number of times '''
	if n <= 0:
		return
	f

# do_n(print_n(2,4),10)

text = raw_input("what is your name?\n")