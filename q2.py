"""
Implement a function named convert_temperature that converts a temperature from Fahrenheit to Celsius or from Celsius to Fahrenheit. 
convert_temperature takes two arguments: temp and unit, which are the temperature and its unit.
"""

def convert_temperature(temp, unit):
  if unit == 'F':
    C = (temp - 32) / 1.8
  elif unit == 'C':
    F = (temp * 1.8) + 32
