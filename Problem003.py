#!/usr/bin/python
import math
import sys
"""
Finds all prime factors of a number
"""
def factorize(x):
    factors = []
    count = 0
    print "[*] Starting factorization..."
    for i in xrange(2, long(math.sqrt(x))):
        if (x % i == 0):
            count += 2
            sys.stdout.flush()
            sys.stdout.write("Found {} factors\r".format(count))
            factors.append(i)
            factors.append(x / i)
    print "[+] Factorization Done"
    return factors

# Fermat's Little Theorem
def isPrime(x):
    prime = True
    for i in range(2,5):
        if ((i**x - i) % x != 0):
            prime = False
            break
    return prime

def primeFactors(x):
    factors = factorize(x)
    pFactors = []
    print "[*] Checking for primes..."
    for i in range(len(factors)):
        if (isPrime(factors[i])):
            pFactors.append(factors[i])
    print "[+] All primes found"
    return pFactors

print primeFactors(600851475143)

