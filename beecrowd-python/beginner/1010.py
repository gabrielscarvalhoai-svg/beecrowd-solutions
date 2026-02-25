"""
Beecrowd Problem 1010 - Simple Calculation
Category: Beginner

Calculates the amount to be paid based on the quantity
and unit price of each item. The input receives two lines,
each with 3 values: item number, quantity, and unit price.
"""


# Input & Processing:

#First line: we use _ for the item code since it's not needed
_, quantity1, unit_value1 = input().split()
total_payable = int(quantity1) * float(unit_value1)

# Second Line: adding directly to the total
_, quantity2, unit_value2 = input().split()
total_payable += int(quantity2) * float(unit_value2)

# Output:
# 'VALOR A PAGAR' means 'AMOUNT TO PAY' in Portuguese
print(f'VALOR A PAGAR: R$ {total_payable:.2f}')
