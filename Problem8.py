#!/usr/bin/python

fileName = "Problem8.txt"
f = open(fileName, 'r')
f_contents = f.readlines()
allDigits = ""
for i in f_contents:
	allDigits += i.rstrip('\r\n')

start = 0
end = 13
largest = 0
while True:
	product = 1
	digits = list(allDigits[start:end])
	intDigits = []
	for digit in digits:
		intDigits.append(int(digit))
	for digit in intDigits:
		product *= digit
	if (product > largest):
		largest = product
	start += 1
	end += 1
	if (end > len(allDigits)):
		break

print "Largest product: " + str(largest)
f.close()
