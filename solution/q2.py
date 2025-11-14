"""
Implement a function named convert_temperature that converts a temperature between Fahrenheit and Celsius. 
convert_temperature takes two arguments: temp and unit, which are the temperature and its unit.
"""

def convert_temperature(temp, unit):
  if unit != "C" and unit != "F":
    return None
  if unit == 'F':
    C = (temp - 32) / 1.8
    return C
  elif unit == 'C':
    F = (temp * 1.8) + 32
    return F
