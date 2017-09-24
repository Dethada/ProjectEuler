#!/usr/bin/python

f = open("Problem013.txt", 'r')
f_contents = f.readlines()
allDigits = []
for i in f_contents:
	allDigits.append((int)(i.rstrip('\r\n')))

print "First 10 digits: " + str(sum(allDigits))[:10]

f.close()
