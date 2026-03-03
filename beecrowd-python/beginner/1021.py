"""
Beecrowd Problem 1021 - Banknotes and Coins
Category: Beginner

This problem reads a monetary value and decomposes it into the minimum
number of banknotes and coins required to represent that amount.

To avoid floating-point precision issues, the value is converted to
cents and processed using integer arithmetic.
"""


money_notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.5, 0.25, 0.10, 0.05, 0.01]


def decompose(txt, values_list, value):
    for n in values_list:
        n = int(round(n * 100))
        quantity = value // n
        value %= n
        print(f'{quantity} {txt} {n/100:.2f}')
    return value


value = int(round(float(input()) * 100))

print('NOTAS:')
remaining = decompose('nota(s) de R$', money_notes, value)

print('MOEDAS:')
decompose('moeda(s) de R$', coins, remaining)
