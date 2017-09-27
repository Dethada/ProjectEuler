#!/usr/bin/python
import sys
from fractions import gcd

# Lowest common multiple
def lcm(a,b):
    return a*b//gcd(a,b)

print reduce(lcm, range(1,20+1))
