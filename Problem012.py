#!/usr/bin/python
from Functions.Functions import factors
import time, itertools

start = time.clock()
for i in itertools.count(1):
    tNum = ((i * (i + 1)) >> 1)
    if len(factors(tNum)) > 500:
        print "Found: {}".format(tNum)
        break

print time.clock() - start
