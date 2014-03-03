#!/usr/bin/python
'''
Exercise 5.3. Fermats Last Theorem says that there are no integers a, b, and c such that
an + bn = cn for any values of n greater than 2.

1. Write a function named check_fermat that takes four parameters a, b, c and n and that
checks to see if Fermats theorem holds. If n is greater than 2 and it turns out to be true that
an + bn = cn the program should print, Holy smokes, Fermat was wrong! Otherwise the program should
print, No, that doesnt work.

2. Write a function that prompts the user to input values for a, b, c and n, converts them to
integers, and uses check_fermat to check whether they violate Fermats theorem.
'''

def check_fermat(a,b,c,n):
	if n > 2:
		if ((a*n) + (b*n)) == (c*n):
			print "Holy smokes, Fermat was wrong!"
			print (a*n), "+", (b*n), " = ", (c*n)
		else:
			print "No, that doesnt work."
			print (a*n), "+", (b*n), " = ", (c*n)
	else:
		print "n has to be larger than 2, you chose:", n

try:
	pass
	# a = int(raw_input("choose the first number: \n"))
	# b = int(raw_input("choose the second number: \n"))
	# c = int(raw_input("choose the third number: \n"))
	# d = int(raw_input("choose n: \n"))
 	# check_fermat(a,b,c,d)
except ValueError:
    print "Could not convert data to an integer."

'''
Exercise 5.4. If you are given three sticks, you may or may not be able to arrange them in a triangle.
For example, if one of the sticks is 12 inches long and the other two are one inch long, it is clear that
you will not be able to get the short sticks to meet in the middle. For any three lengths, there is a
simple test to see if it is possible to form a triangle:

If any of the three lengths is greater than the sum of the other two, then you cannot
form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
form what is called a “degenerate” triangle.)

1. Write a function named is_triangle that takes three integers as arguments, and that prints
either “Yes” or “No,” depending on whether you can or cannot form a triangle from sticks
with the given lengths.

2. Write a function that prompts the user to input three stick lengths, converts them to integers,
'''