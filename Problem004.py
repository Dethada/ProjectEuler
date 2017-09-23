#!/usr/bin/python

# Finds largest palindromic number that is a product of 2 3digit numbers

def isPalindromic(x):
    strX = list(str(x))
    reversedX = strX[::-1]
    if (strX == reversedX):
        return True
    else:
        return False

largest = 0
print "[*] Finding palindromics"
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if (isPalindromic(product)):
            if (product > largest):
                largest = product

print "Largest palindromic: " +  str(largest)

