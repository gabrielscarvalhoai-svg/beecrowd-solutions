"""
Beecrowd Problem 1014 - Consumption
Category: Beginner

This problem calculates fuel consumption in kilometers per liter (km/L),
the standard unit used in Brazil and most countries.

In countries such as the United States, fuel efficiency is typically
measured in miles per gallon (MPG).
"""


distance = int(input())
fuel = float(input())

# Fuel consumption in km/L (kilometers per liter)
# 1 mile = 1.60934 km
# 1 gallon (US) = 3.78541 liters
consumption = distance / fuel

print(f'{consumption:.3f} km/l')
