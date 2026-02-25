"""
Beecrowd Problem 1008 - Salary
Category: Beginner
Calculate an employee's salary based on hours worked
and their hourly rate, displaying the employee's number.
"""


# Input:
employee_number = int(input())
hours_worked = int(input())
hourly_rate = float(input())

# Processing:
salary = hours_worked * hourly_rate

# Output:
print(f'NUMBER = {employee_number}')
print(f'SALARY = U$ {salary:.2f}')
