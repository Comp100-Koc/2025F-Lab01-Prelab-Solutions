# 2025F-Lab01-Prelab-Solutions

This prelab has 6 questions. In each question, you are asked to implement a specific function. You must implement each function in the corresponding file. In other words, you should implement the function for Question 1 in `q1.py`, the function for Question 2 in `q2.py` and so on.

You can run the `test.py` file to check whether your implementation is correct or not.
Remember that the testcases inside the `test.py` are just sample testcases, and additional testcases will be used while grading.

**DO NOT MODIFY THE `test.py` FILE.**


**Hint: In order to calculate the square root of a number, you can raise it to the power of 0.5**

## Question 1
In this question, we want to implement a python function that calculates the mathematical function `f(x) = (5x-3) / (2x+6)`.

Implement a function named `calculate_f`, which takes `x` as an argument, and returns `(5x-3) / (2x+6)`.

### Examples:
`calculate_f(3)` should return `1.0`

`calculate_f(6)` should return `1.5`

`calculate_f(15.0)` should return `2.0`


## Question 2
Implement a function named `to_celcius` that converts a temperature from Fahrenheit to Celsius. It takes one argument: `f`, which is the temperature in Fahrenheit. This function should return the temperature in Celcius.

### Formula:
The conversion from Fahrenheit to Celcius follows this formula:

\[
C = $(F - 32) / 1.8$
\]

where C is the temperature in Celcius, F is the temperature in Fahrenheit.

### Examples: 
`to_celcius(32)` should return `0.0`

`to_celcius(75)` should return `28.89`

## Question 3
A quadratic equation is an equation of the form $ax^2+bx+c=0$.

One of the solutions of the quadratic equation is $$x=\frac{-b-\sqrt{b^2-4ac}}{2a}$$

Implement a function named `solve_quadratic` which takes three arguments: `a`, `b`, and `c`, which are the coefficients of the quadratic equation. This function should return the solution written above. You can assume that the quadratic equation will always have a solution.



**Note:** For a quadratic equation, $x=\frac{-b+\sqrt{b^2-4ac}}{2a}$ is also a solution. However, please ignore this and only return the solution written above.

### Examples: 
`solve_quadratic(1, -5, 6)` should return `2.0`

`solve_quadratic(5, -33, 50.4)` should return `2.4`


## Question 4


In this question, we want to calculate the Euclidean distance between two points in a 2D plane.

Implement a function named `calculate_distance`, which takes four arguments: `x1`, `y1`, `x2`, and `y2`, representing the coordinates of two points `(x1, y1)` and `(x2, y2)`. This function should return the Euclidean distance between these two points.

### Formula:
The Euclidean distance between two points \((x_1, y_1)\) and \((x_2, y_2)\) is given by:

\[
d = $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
\]

### Examples:
`calculate_distance(-2, -2, -2, -2)` should return `0`

`calculate_distance(0, 3, 4, 0)` should return `5.0`

`calculate_distance(3, 5, 9, 13)` should return `10`

## Question 5

In this question, we want to calculate the area of a triangle, given the length of its three sides.

Implement a function named `calculate_area`, which takes three arguments: `a`, `b`, and `c`, which are the lengths of the three sides. This function should return the area of the triangle.

**Hint:** You can use [Heron's formula](https://en.wikipedia.org/wiki/Heron%27s_formula) to calculate the area.

### Examples:
`calculate_area(6.25, 4.25, 6.5)` should return `12.75`

`calculate_area(20.5, 20.5, 9)` should return `90.0`
