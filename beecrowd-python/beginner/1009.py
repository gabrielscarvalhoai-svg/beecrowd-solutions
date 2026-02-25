"""
Beecrowd Problem 1009 - Salary with bonus
Category: Beginner

It calculates how much the salesperson should receive
based on their fixed salary, plus a 15% bonus on sales
made during the month.

"""

# Input:
employee_name = input().strip()
fixed_salary = float(input().strip())
total_sales = float(input().strip())

# Processing:
final_total = fixed_salary + (total_sales * 0.15)

# Output:
print(f'TOTAL = R$ {final_total:.2f}')
