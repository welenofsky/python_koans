#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # Sort so I know where the big nums and small nums are
    sides = sorted([a,b,c])
    # Helps identify how many sides are the same length
    set_len = len(set(sides))

    if (sides[0] < 1):
        # If any of the sides are less than 1
        raise TriangleError
    elif ((sides[0] + sides[1]) < sides[2]):
        # If not valid triangle
        raise TriangleError
    
    # Identify Triangle Type
    if (set_len == 1):
        return 'equilateral'
    elif (set_len == 2):
        return 'isosceles'

    # 3 sides are unique
    return 'scalene'

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
