#!/usr/bin/python
from math import factorial

# central binomial coefficient
n = 20
ans = int(factorial(2 * n) / (factorial(n) ** 2))

print ans
