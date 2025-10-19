# 2025F-Lab01-Prelab

This prelab has 2 questions. In each question, you are asked to implement a specific function. You must implement each function in the corresponding file. In other words, you should implement the function for Question 1 in `q1.py`, the function for Question 2 in `q2.py` and so on.

You can run the `test.py` file to check whether your implementation is correct or not.
Remember that the testcases inside the `test.py` are just sample testcases, and additional testcases will be used while grading.

**DO NOT MODIFY THE `test.py` FILE.**

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/qDWf2xfs)

*Hint: In order to calculate the square root of a number, you can raise it to the power of 0.5*

## Question 1 (25 Points)

### Part a

In this question, we want to calculate the Euclidean distance between two points in a 2D plane.

Implement a function named `distance`, which takes four arguments: `x1`, `y1`, `x2`, and `y2`, representing the coordinates of two points `(x1, y1)` and `(x2, y2)`. This function should return the Euclidean distance between these two points.

#### Formula:
The Euclidean distance between two points \((x_1, y_1)\) and \((x_2,
y_2)\) is given by: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$


#### Examples:

```python
distance(-2, -2, -2, -2) # should return 0
distance(0, 3, 4, 0) # should return 5.0
distance(3, 5, 9, 13) # should return 10
```

### Part b

In this question, we want to calculate the area of a triangle, given the length of its three sides.

Implement a function named `area_from_sides`, which takes three arguments: `a`, `b`, and `c`, which are the lengths of the three sides. This function should return the area of the triangle.

You can use [Heron's formula](https://en.wikipedia.org/wiki/Heron%27s_formula) to calculate the area.

#### Examples:
```python
area_from_sides(6.25, 4.25, 6.5) # should return 12.75

area_from_sides(20.5, 20.5, 9) # should return 90.0
```

### Part c

In this question, we want to calculate the area of a triangle given
the (x, y) coordinates of its three vertices. 

Implement a function named `area_from_vertices`, which takes six
arguments: `x1`, `y1`,  `x2`, `y2`, `x3`, `y3`

You *must re-use* the functions you've already written in parts a and b, because
functions are ment to be re-used to make things easier.

**Hint:** 

1. First calculate the three sides by calling the `distance`
function you wrote in Question 2 on each pair of vertices. Assign the results to intermediate
variables; for example `s12`, `s13`, `s23` 

2. Then use the `area_from_sides` function you wrote in Question 3

3. Make sure to *return* the final result!

#### Examples:

```python
area_from_vertices(0, 0, 3, 0, 0, 4) # should return 6

area_from_vertices(-3.5, 0, 3.5, 0, 0, 5) # should return 17.5
```

## Question 2: Temperature Converter (25 Points)

Write a function `convert_temperature` that converts temperatures
between Fahrenheit and Celcius. The function should take two
parameters: the temperature to convert and the unit of the input
temperature ('F' for Fahrenheit, 'C' for Celsius). Based on these
parameters, the function should return the converted temperature.

### Requirements:

- Use `if-else` statements to determine the direction of the conversion.
- Round the result to 2 decimal places.
- If an invalid unit is provided, return `None`

### Formulae:

- Celsius to Fahrenheit: `F = (C * 1.8) + 32`

- Fahrenheit to Celsius: `C = (F - 32) / 1.8`

- You may find the `round` function useful. It takes a float f, and an
  integer n as arguments and returns f rounded to n places. E.g
  `round(2.6786, 3)` returns `2.679`
  
### Example Usage:

```python
print(convert_temperature(100, 'C')) # Output: 212.0
print(convert_temperature(32, 'F')) # Output: 0.0
print(convert_temperature(20, 'X')) # Output: None
```


## Question 3 (Bonus Question)
A quadratic equation is an equation of the form $ax^2+bx+c=0$.

One of the solutions of the quadratic equation is $$x=\frac{-b-\sqrt{b^2-4ac}}{2a}$$

Implement a function named `solve_quadratic` which takes three arguments: `a`, `b`, and `c`, which are the coefficients of the quadratic equation. This function should return the solution written above. You can assume that the quadratic equation will always have a solution.



**Note:** For a quadratic equation, $x=\frac{-b+\sqrt{b^2-4ac}}{2a}$ is also a solution. However, please ignore this and only return the solution written above.

### Examples: 
```python
solve_quadratic(1, -5, 6) # should return 2.0
solve_quadratic(5, -33, 50.4) # should return 2.4
```
