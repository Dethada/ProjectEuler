#!/usr/bin/python
from time import clock

start = clock()
limit = 9**5*(5-1)
numbers = []
for i in range(2, limit):
    listI = str(i)
    powSum = 0
    for digit in listI:
        powSum += int(digit)**5
    if powSum == i:
        numbers.append(i)

print "Numbers: {}\nSum: {}".format(numbers, sum(numbers))
print clock() - start
