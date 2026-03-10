"""
Beecrowd Problem 1041 - Coordinates of a Point
Category: Beginner

This problem reads two floating-point values representing
the coordinates (x, y) of a point in a Cartesian plane.

The program determines whether the point is located at the origin,
on one of the axes, or in one of the four quadrants.
"""


x, y = map(float, input().split())

if x == 0 and y == 0:
    print('Origem')
elif x == 0:
    print('Eixo Y')
elif y == 0:
    print('Eixo X')
elif x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
else:
    print('Q4')
