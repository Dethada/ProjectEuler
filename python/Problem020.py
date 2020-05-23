#!/usr/bin/python
import math

digits = str(math.factorial(100))

total = 0

for i in digits:
    total += int(i)

print "Total: {}".format(total)
