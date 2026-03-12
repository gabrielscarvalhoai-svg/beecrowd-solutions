"""
Beecrowd Problem 1042 - Simple Sort
Category: Beginner

This problem reads three integer values and prints them
in ascending order.

After printing the sorted values, the program prints
a blank line followed by the original values in the
same order they were read.
"""


list_numbers = [int(x) for x in input().split()]

sorted_numbers = sorted(list_numbers)

for x in sorted_numbers:
    print(x)
print()
for i in list_numbers:
    print(i)
