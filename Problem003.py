#!/usr/bin/python
import math, sys, time
from Functions.Functions import Functions
"""
Finds all prime factors of a number
"""
start = time.clock()
factors = Functions.factorize(600851475143)
pFactors = []
for factor in factors:
    if (Functions.isPrime(factor)):
        pFactors.append(factor)

print pFactors
print time.clock() - start
