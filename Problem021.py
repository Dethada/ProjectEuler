#!/usr/bin/python
from Functions import Functions
import time

pairs = []

def d(n):
    factors = set()
    factors.update(Functions.factors(n))
    factors.remove(n)
    return sum(factors)

def check(n):
    for i in pairs:
        for x in i:
            if x == n:
                return True
    return False

start = time.clock()
for a in range(200, 10000):
    b = d(a)
    if d(b) == a and a != b and not check(a) and not check(b):
        print "Pair found: {} and {}".format(a,b)
        pairs.append([a, b])

ans = sum([sum(i) for i in pairs])

print "Ans: {}".format(ans)
print time.clock() - start
