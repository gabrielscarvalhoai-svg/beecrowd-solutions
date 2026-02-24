"""
Beecrowd Problem 1006 - Average 2
Category: Beginner
Calculate the weighted average of a student's three grades (A, B and C),
as requested by the exercise.
"""


# Input
A = float(input())
B = float(input())
C = float(input())

# Processing
# Sum of weights: 2.0 + 3.0 + 5.0 = 10.0
weighted_average = ((A * 2.0) + (B * 3.0) + (C * 5.0)) / 10.0

# Output
# MEDIA is the Portuguese word for Average
print(f'MEDIA = {weighted_average:.1f}')
