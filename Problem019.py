#!/usr/bin/python

monthDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def isLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

def isSunday(day):
    if (day % 7 == 0):
        return True
    return False

days = 0
count = 0

# iterate through years
for i in range(100):
    if isLeap(1901 + i):
        monthDays[2] = 29
    else:
        monthDays[2] = 28
    # iterate through months
    for j in range(1, 13):
        if (isSunday(days)):
            count += 1
        days += monthDays[j]


print "Number of Sundays: {}".format(count)
