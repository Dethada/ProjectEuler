#!/usr/bin/python
import time

# Carmichael numbers
carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153]

# Fermat's Little Theorem
def isPrime(x):
	prime = True
	if (x in carmichael):
		return False
	for i in range(2,10):
		if ((i**x - i) % x != 0):
			prime = False
			break
	return prime

num = 2
ans = 0
n = 10001 # to find nth prime
y = n -1
start = time.time()
for i in range(n):
	while True:
		if (isPrime(num)):
			if (i == y):
				ans = num
			num += 1
			break
		num += 1

print str(n) + " prime: " + str(ans)
print(time.time() - start)
