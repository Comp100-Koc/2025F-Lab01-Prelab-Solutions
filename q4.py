"""
Implement a function named calculate_distance, which takes four arguments: x1, y1, x2, and y2, representing the coordinates of two points (x1, y1) and (x2, y2). 
This function should return the Euclidean distance between these two points.
"""

def calculate_distance(x1, y1, x2, y2):
  distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
  return distance
