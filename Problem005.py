#!/usr/bin/python
import sys
"""
Smallest positive number that is evenly divisible by all of the numbers 
from 1 to 20
Takes about 2 minutes to finish
"""
divisible = True
i = 2520
print "[*] Finding number..."
while True:
    for j in range(1, 22):
        if (j == 21):
            print "Found number: " + str(i)
            sys.exit(0)
        elif (i % j != 0):
            divisible = False
            i += 1
            break

