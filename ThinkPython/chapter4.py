#!usr/bin/python

from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
#print bob

#for i in range(4):
#	fd(bob, 100)
#	lt(bob)

# wait_for_user()

'''
1. Write a function called square that takes a parameter named t, which is a turtle. It
should use the turtle to draw a square.
Write a function call that passes bob as an argument to square, and then run the
program again.
2. Add another parameter, named length, to square. Modify the body so length of the
sides is length, and then modify the function call to provide a second argument. Run
the program again. Test your program with a range of values for length.
3. The functions lt and rt make 90-degree turns by default, but you can provide a
second argument that specifies the number of degrees. For example, lt(bob, 45)
turns bob 45 degrees to the left.
Make a copy of square and change the name to polygon. Add another parameter
named n and modify the body so it draws an n-sided regular polygon. Hint: The
exterior angles of an n-sided regular polygon are 360/n degrees.
4. Write a function called circle that takes a turtle, t, and radius, r, as parameters and
that draws an approximate circle by invoking polygon with an appropriate length
and number of sides. Test your function with a range of values of r.
5. Make a more general version of circle called arc that takes an additional parameter
angle, which determines what fraction of a circle to draw. angle is in units of degrees,
so when angle=360, arc should draw a complete circle.
'''

def square(t,l):
	for i in range(4):
		fd(t,l)
		lt(t)

def polygon(t,l,n):
	turn_degree = 360/n
	for i in range(n):
		fd(t,l)
		lt(t,turn_degree)

def circle(t,r):
	from math import pi
	circum = 2 * pi * r
	t.delay = .01
	polygon(t,circum/360,360)

def arc(t,r,a):
	from math import pi
	t.delay = .01

	circum = 2 * pi * r
	move = circum/360
	turn_degree = 1

	for i in range(a):
		fd(t,move)
		lt(t,1)


# print bob
# arc(bob,r=25,a=180)

# wait_for_user()