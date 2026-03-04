"""
Beecrowd Problem 1037 - Interval
Category: Beginner

This problem reads a floating-point number and determines
which interval it belongs to among the following:

[0,25], (25,50], (50,75], (75,100]

If the value does not belong to any of these intervals,
the program prints "Fora de intervalo".

The interval notation follows mathematical convention,
where brackets indicate inclusion and parentheses indicate exclusion.
"""


value = float(input())

if value < 0 or value > 100:
    print('Fora do intervalo')
elif value <= 25:
    print('Intervalo ([0, 25]')
elif value <= 50:
    print('(25, 50]')
elif value <= 75:
    print('(50, 75]')
else:
    print('Intervalo (75, 100])')
