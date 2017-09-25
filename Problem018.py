#!/usr/bin/python

# reference https://stackoverflow.com/questions/8002252/euler-project-18-approach

triangle = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

tmp = {0:75, 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:triangle[14]}

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
