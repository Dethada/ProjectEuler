#!/usr/bin/python
from sympy import isprime
from Functions.Functions import Functions
from time import clock

# http://www.mathblog.dk/project-euler-27-quadratic-formula-primes-consecutive-values/

start = clock()
highest = 0
max_a = 0
max_b = 0
primes = Functions.sieve(1000)
for a in range(-999, 1000, 2):
    for b in primes:
        for n in range(100):
            if not isprime(n**2 + a*n + b):
                count = n + 1
                if count > highest:
                    highest = count
                    max_a = a
                    max_b = b
                break

print "a={}\nb={}\nProduct={}\nCount={}\n".format(max_a, max_b, max_a * max_b, highest)
print clock() - start
