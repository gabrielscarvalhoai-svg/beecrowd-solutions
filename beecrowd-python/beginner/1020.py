"""
Beecrowd Problem 1020 - Age in Days
Category: Beginner

This problem converts a given number of days into years,
months, and remaining days, assuming 1 year = 365 days
and 1 month = 30 days.
"""


total_days = int(input())

years = total_days // 365
remaining = total_days % 365
months = remaining // 30
days = remaining % 30

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')
