#!/usr/bin/python

prevNums = [1, 2]
fibNum = prevNums[0] + prevNums[1]
index = 4

while True:
    prevNums[0] = prevNums[1]
    prevNums[1] = fibNum
    fibNum = prevNums[0] + prevNums[1]
    index += 1

    if (len(str(fibNum)) == 1000):
        break

print "Fibonacci number: {}\nIndex: {}".format(fibNum, index)
