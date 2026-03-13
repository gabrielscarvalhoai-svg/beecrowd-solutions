"""
Beecrowd Problem 1044 - Multiples
Category: Beginner

This problem reads two integer values and determines
whether one is a multiple of the other.

If the larger number is divisible by the smaller one,
the numbers are multiples. Otherwise, they are not.
"""


a, b = map(int, input().split())

bigger = max(a, b)
smaller = min(a, b)

if bigger % smaller == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
