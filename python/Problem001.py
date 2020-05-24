#!/usr/bin/env python3

# prev = 0
# for i in range(100):
#     if (i % 3 == 0 or i % 5 == 0):
#         print(i - prev, end=', ')
#         prev = i
# exit()

def solve(n):
    tmp = n - 1
    three_term = tmp // 3
    five_term = tmp // 5
    fifteen_term = tmp // 15
    total = 3 * (three_term * (three_term + 1) // 2)
    total += 5 * (five_term * (five_term + 1) // 2)
    total -= 15 * (fifteen_term * (fifteen_term + 1) // 2)
    # print(three_term, five_term, fifteen_term)
    print(total)
    return total

solve(10)
solve(100)
solve(1000)
solve(1000000000)