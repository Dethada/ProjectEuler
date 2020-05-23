#!/usr/bin/python
import math, sys, time
from Functions.Functions import Functions
from sympy import isprime
"""
Finds all prime factors of a number
"""
start = time.clock()
factors = Functions.factorize(600851475143)
pFactors = []

def pFactor(factor):
    if (isprime(factor)):
        pFactors.append(factor)

map(pFactor, factors)

print pFactors
print time.clock() - start
