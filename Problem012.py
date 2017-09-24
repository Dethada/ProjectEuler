#!/usr/bin/python
import math

# returns number of factors of x
def factorize(x):
    factors = []
    count = 0
    for i in xrange(2, long(math.sqrt(x))):
        if (x % i == 0):
            count += 2
    return count

i = 1
while True:
    tNum = ((i * (i + 1)) / 2)
    if factorize(tNum) > 500:
        print "Found: " + str(tNum)
        break
    else:
        i += 1
