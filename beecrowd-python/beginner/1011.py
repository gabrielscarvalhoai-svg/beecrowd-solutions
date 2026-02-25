"""
Beecrowd Problem 1011 - Sphere
Category: Beginner

Calculate the volume of a sphere using its radius (R),
with the formula 4/3 * pi * R³.
"""


# Input: 
R = float(input())
pi = 3.14159

# Processing:
volume = (4/3.0) * pi * (R ** 3)

# Output:
print(f'VOLUME = {volume:.3f}')
