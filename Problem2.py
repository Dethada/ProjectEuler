#!/usr/bin/python

prevNums = [1, 2]
fibNum = prevNums[0] + prevNums[1]
evenSum = 2

while (fibNum < 4000000):
    prevNums[0] = prevNums[1]
    prevNums[1] = fibNum
    fibNum = prevNums[0] + prevNums[1]

    if (fibNum % 2 == 0):
        evenSum += fibNum

print evenSum

