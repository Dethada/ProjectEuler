#!/usr/bin/python

sumNums = 0
sqSum = 0

print "[*] Interating 1 - 100..."
for i in range(1, 101):
    sumNums += i
    sqSum += i**2

print "[*] Squaring sum of 1 to 100"
sumNumsSq =  sumNums ** 2
print "Difference: " + str(sumNumsSq - sqSum)

