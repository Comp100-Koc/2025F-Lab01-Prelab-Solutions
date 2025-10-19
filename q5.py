"""
Implement a function named calculate_area, which takes three arguments: a, b, and c, which are the lengths of the three sides. 
This function should return the area of the triangle.
"""

def calculate_area(a, b, c):
  s = 0.5 * (a+b+c)
  A = (s*(s-a)*(s-b)*(s-c))**0.5
  return A
