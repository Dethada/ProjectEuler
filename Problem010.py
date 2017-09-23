#!/usr/bin/python
import time

start = time.time()
print "[*] Finding primes below 2 million..."
def sieve(limit):
	sieve = [True] * limit
	def mark(sieve, x):
		for i in xrange(x+x, len(sieve), x):
			sieve[i] = False

	for x in xrange(2, int(len(sieve) ** 0.5) + 1):
		if sieve[x]:
			mark(sieve, x)

	return sum(i for i in xrange(2, len(sieve)) if sieve[i]) 

print "Sum: " + str(sieve(2000000))
print "Done in: " + str(time.time() - start)
