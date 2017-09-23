#!/usr/bin/python
"""
using bruteforce for now
a and c are always odd; b is always even
formula that can be implemented
a = 2pq
b = p2 - q2
c = p2 + q2
p and q must be odd integers, with p > q, and with no common divisors
p and q cannot both be odd
http://www.friesian.com/pythag.htm
"""
def pythagoreanTriples(limit):
	triplets = []
	for a in range(1, limit, 2):
		for b in range(0, limit, 2):
			for c in range(1, limit, 2):
				if (a ** 2 + b ** 2 == c ** 2):
					triplets.append([a, b, c])
	return triplets

triplets = pythagoreanTriples(1000)
for i in triplets:
	sum = 0
	for j in i:
		sum += j
	if (sum == 1000):
		print "Found triplet: " + str(i)
		print "Product: " + str(i[0] * i[1] * i[2])
		break
