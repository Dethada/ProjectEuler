#!/usr/bin/python

digits = str(2 ** 1000)
total = 0

for digit in digits:
    total += int(digit)

print total
