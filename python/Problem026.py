#!/usr/bin/python
from Functions.Functions.Functions import sieve
from time import clock
import sys

for d in sieve(1000)[::-1]:
    period = 1
    while pow(10, period) % d != 1: period += 1
    if d-1 == period:
        print d 
        sys.exit()
