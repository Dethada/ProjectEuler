#!/usr/bin/python
from Functions import Functions
import math, time

def isAbundant(n):
    factors = []
    factors.extend(Functions.factors(n))
    factors.remove(n)
    if sum(factors) > n:
        return True
    return False

total = 0
abundantNums = set()
abundantNumsL = []

start = time.clock()
for i in range(1, 28124):
	abundant_sum = False
	if isAbundant(i):
		abundantNums.add(i)
        abundantNumsL.append(i)
	for num in abundantNumsL:
		if (i - num) in abundantNums:
			abundant_sum = True
			break
	if not abundant_sum:
		total += i

print "Sum: {}".format(total)
print(time.clock() - start)
