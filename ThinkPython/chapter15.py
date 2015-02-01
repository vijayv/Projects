#!/usr/bin/python

'''
Exercise 15.1. Write a function called distance_between_points
that takes two Points as arguments and returns the distance between them.
'''
def distance_between_points(p1, p2):
    import math

    v1 = (p1['x'] - p2['x'])**2
    v2 = (p1['y'] - p2['y'])**2

    return math.sqrt(v1 + v2)

'''
Exercise 15.2
'''

class Point(object):
  '''Represents a point in 2-D space.'''


if __name__ == '__main__':

    p1 = {'x' : 1, 'y' : 4}
    p2 = {'x' : 4, 'y' : 2}

    print distance_between_points(p1, p2)

    blank = Point()
    blank.x = 3.0
    blank.y = 5.0
    print "Printing ", blank
    print "Coor x: ", blank.x
