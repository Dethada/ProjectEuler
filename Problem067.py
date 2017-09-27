#!/usr/bin/python

f = open("Problem067.txt", 'r')
f_contents = f.readlines()
triangle = [i.rstrip('\r\n') for i in f_contents]
triangle = [i.split(" ") for i in triangle]
triangle = [map(int, x) for x in triangle]

numbers = range(100)
tmp = {key: [] for key in numbers}
tmp[0] = triangle[0]
tmp[99] = triangle[99]

# prev row can access [index] and [index+1]
for i in range(len(triangle)-1, -1, -1):
    if i != (len(triangle) - 1) and i != 0:
        for j in range(len(triangle[i])):
            # comparing adj numbers from row below & add the larger number
			if tmp[i+1][j] > tmp[i+1][j+1]:
				tmp[i].append(tmp[i+1][j] + triangle[i][j])
			else:
				tmp[i].append(tmp[i+1][j+1] + triangle[i][j])

tmp[0] = max(tmp[1]) + triangle[0][0]

print "Highest: {}".format(tmp[0])
f.close()
