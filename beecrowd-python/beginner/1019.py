"""
Beecrowd Problem 1019 - Time Conversion
Category: Beginner

This problem converts a given number of seconds into hours,
minutes, and remaining seconds.
"""


total_seconds = int(input())

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f'{hours}:{minutes}:{seconds}')
