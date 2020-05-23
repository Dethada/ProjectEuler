#!/usr/bin/python

fileName = "Problem022.txt"
f = open(fileName, 'r')
f_contents = f.readlines()
f_contents = f_contents[0].split(",")
names = []

for name in f_contents:
    names.append(name[1:-1])

names.sort()
total = 0

for i, name in enumerate(names):
    tmp = 0
    for char in name:
        tmp += ord(char) - 64
    total += tmp * (i + 1)

print "Total name scores: {}".format(total)

f.close()
