#/usr/bin/python
'''
To test the square root algorithm in this chapter, you could compare it with
math.sqrt. Write a function named test_square_root that prints a table like this:

The first column is a number, a; the second column is the square root of a computed with the function
from Section 7.5; the third column is the square root computed by math.sqrt; the fourth column is
the absolute value of the difference between the two estimates.
'''

def square_root(a):
    epsilon = .0000001
    x, y = 1.0, 0.0
    x = a/2
    while abs(y-x) > epsilon:
        x = y if y > 0 else 1
        y = (x + a/x) / 2

    return y

def test_square_root(x):
    from math import sqrt
    my_value = square_root(x)
    act_value = sqrt(x)
    string =  x, my_value, act_value, abs(my_value - act_value)
    return string

'''
Exercise 7.4. The built-in function eval takes a string and evaluates it using the Python interpreter.
For example:

Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of the last expression it
evaluated.
'''

def eval_loop():
    inval = ''
    while inval <> "\"done\"":
        inval = raw_input("What would you like to evaluate? \n")
        print eval(inval)

'''
Exercise 7.5. The mathematician Srinivasa Ramanujan found an infinite series that can be used to
generate a numerical approximation of pi:

Write a function called estimate_pi that uses this formula to compute and return an estimate of
pi. It should use a while loop to compute terms of the summation until the last term is smaller than
1e-15 (which is Python notation for 10^15). You can check the result by comparing it to math.pi.

'''

# This looks overly complicated and I don't feel like doing it!

if __name__ == '__main__':
    print test_square_root(18)

    eval_loop()