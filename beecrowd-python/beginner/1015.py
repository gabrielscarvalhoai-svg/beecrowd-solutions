"""
Beecrowd Problem 1015 - Distance Between Two Points
Category: Beginner

This problem reads the coordinates of two points in a Cartesian plane
and calculates the Euclidean distance between them using the formula:

distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
"""


from math import sqrt


x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

distance = sqrt(dx ** 2 + dy ** 2)

print(f'{distance:.4f}')
