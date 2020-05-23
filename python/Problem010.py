#!/usr/bin/python
import time, math
from Functions.Functions import Functions

start = time.time()
print "Sum: {}".format(sum(Functions.sieve(2000000)))
print "Done in: " + str(time.time() - start)
