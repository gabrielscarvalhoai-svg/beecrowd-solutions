"""
Beecrowd Problem 1043 - Triangle
Category: Beginner

This problem reads three floating-point values representing
the lengths of three line segments.

If the values can form a triangle (based on the triangle
inequality rule), the program calculates and prints the
perimeter of the triangle.

Otherwise, the program calculates the area of a trapezoid
using the formula ((A + B) * C) / 2.
"""


a, b, c = map(float, input().split())

if a + b > c and b + c > a and a + c > b:
    perimeter = a + b + c
    print(f'Perimetro = {perimeter:.1f}')
else:
    area = ((a + b) * c) / 2
    print(f'Area = {area:.1f}')
