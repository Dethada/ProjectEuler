#!/usr/bin/python
from Functions.Functions import Functions
from sympy import isprime

def next_permutation(arr):
	# Find non-increasing suffix
	i = len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i <= 0:
		return False
	
	# Find successor to pivot
	j = len(arr) - 1
	while arr[j] <= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Reverse suffix
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True

primes = [i for i in Functions.sieve(10000) if i > 1000]

for prime in primes:
    arr = list(str(prime))
    permutations = set()

    # get all prime permutations of the prime
    while next_permutation(arr):
        x = int("".join(map(str, arr)))
        if isprime(x):
            permutations.add(x)
    
    for perm in permutations:
        diff = perm - prime
        prime3 = perm + diff
        if isprime(prime3):
            if prime3 in permutations:
                print "Found: {}, {}, {}".format(prime, perm, prime3)
