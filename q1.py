"""
Part a) Implement a function named distance, which takes four arguments: x1, y1, x2, and y2, representing the coordinates of two points (x1, y1) and (x2, y2). 
This function should return the Euclidean distance between these two points.

Part b) Implement a function named area_from_sides, which takes three arguments: a, b, and c, which are the lengths of the three sides. 
This function should return the area of the triangle.

Part c) Implement a function named area_from_vertices, which takes three arguments: x1, y1, x2, y2, x3, y3, which are the coordinates of the vertices of a triangle. 
This function should return the area of the triangle.
"""

def distance(x1, y1, x2, y2):
  distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
  return distance

def area_from_sides(a, b, c):
  s = 0.5 * (a+b+c)
  A = (s*(s-a)*(s-b)*(s-c))**0.5
  return A


def area_from_vertices(x1, y1, x2, y2, x3, y3):
  side1 = distance(x1, y1, x2, y2)
  side2 = distance(x1, y1, x3, y3)
  side3 = distance(x2, y2, x3, y3)
  area = area_from_sides(side1, side2, side3)
  return area
