#!/usr/bin/python

ones = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
tens = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
twenties = {2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
hundreds = {1:13, 2:13, 3:15, 4:14, 5:14, 6:13, 7:15, 8:15, 9:14}

# hundred = 7, and = 3, hundredand = 10, onethousand = 11
total = 0

# 1 - 9
for i in range(1, 10):
    total += ones[i]

# 10 - 19
for i in range(10, 20):
    total += tens[i]

# 20 - 99
for i in range(2, 10):
    total += twenties[i] # adds 20,30,40...
    for j in range(1, 10):
        total += twenties[i] + ones[j] # 21 - 99 excluding 30,40,50...

tmp = total

# 100 - 999
for i in range(1, 10):
    total += hundreds[i] - 3
    total += (99 * hundreds[i]) + tmp

# 1000
total += 11

print "Total letters used: {}".format(total)
