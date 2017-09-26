from cpython cimport bool
from math import sqrt

# Carmichael numbers
cdef carmichael = set([561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153])

# Fermat's Little Theorem
def isPrime(long x):
    if (x in carmichael):
        return False
    for i in range(2,10):
        if ((i**x - i) % x != 0):
            return False
    return True

# Sieve of Eratosthenes
# limit is the highest number it sieves to not the number of primes it returns
cdef void mark(list sieve, long x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

def sieve(long limit):
    cdef list sieve = [True] * limit
    cdef list primes = []

    for x in xrange(2, int(sqrt(len(sieve))) + 1):
        if sieve[x]:
            mark(sieve, x)

    primes.extend(i for i in xrange(2, len(sieve)) if sieve[i])
    return primes

# generate triangle numbers up to a limit
def triangleNumbers(long limit):
    cdef list numbers = []
    for i in range(1, limit + 1):
        numbers.append((i * (i + 1)) >> 1)
    return numbers

# returns number of factors of x
def noOfFactors(long x):
    cdef list factors = []
    cdef int count = 0
    for i in xrange(2, long(sqrt(x))):
        if (x % i == 0):
            count += 2
    return count

# returns all factors of x except for 1 and x itself
def factorize(long x):
    cdef list factors = []
    cdef int count = 0
    cdef long i
    for i in xrange(2, long(sqrt(x))):
        if (x % i == 0):
            count += 2
            factors.append(i)
            factors.append(x / i)
    return factors

# returns all factors of n
def factors(long n):    
    return set(reduce(list.__add__, 
    ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))
