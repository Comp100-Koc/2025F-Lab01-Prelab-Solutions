"""
Implement a function named solve_quadratic which takes three arguments: a, b, and c, which are the coefficients of the quadratic equation. 
This function should return the solution written in readME file. You can assume that the quadratic equation will always have a solution.
"""

def solve_quadratic(a, b, c):
  x = (-1 * b - (b**2 - 4*a*c)**0.5) / (2*a)
  return x
