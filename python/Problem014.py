#!/usr/bin/python

longestCount = 0
longestStart = 0
for start in range(2, 1000000):
    n = start
    count = 1
    while n != 1:
        if (n % 2 == 0):
            n /= 2
            count += 1
        else:
            n = ((3 * n) + 1) / 2
            count += 2
    if count > longestCount:
        longestStart = start
        longestCount = count

print "Longest chain (start): " + str(longestStart)
print "Longest chain (count): " + str(longestCount)
