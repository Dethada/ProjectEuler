#!/usr/bin/python
import time
from Functions.Functions import Functions

num = 2
ans = 0
n = 10001 # to find nth prime
y = n -1
start = time.time()
for i in range(n):
	while True:
		if (Functions.isPrime(num)):
			if (i == y):
				ans = num
			num += 1
			break
		num += 1

print str(n) + " prime: " + str(ans)
print(time.time() - start)
