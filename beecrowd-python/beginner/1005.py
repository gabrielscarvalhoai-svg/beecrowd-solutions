"""
Beecrowd Problem 1005 - Average 1
Category: Beginner
Calculating the weighted average between a student's two grades,
as requested by the exercise.
"""


# Input
A = float(input())
B = float(input())

# Processing
# Sum of weights: 3.5 + 7.5 = 11.0
weighted_average = ((A * 3.5) + (B * 7.5)) / 11

# Output
# MEDIA means Average in Portuguese
print(f'MEDIA = {weighted_average:.5f}')
