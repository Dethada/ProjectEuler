#!/usr/bin/env python3
import random
import string

def generate(n_max, ab_len):
    n = random.randrange(n_max)

    a_len = random.randrange(ab_len)
    b_len = random.randrange(ab_len)
    a = ''.join(random.choice(string.digits) for _ in range(a_len))
    b = ''.join(random.choice(string.digits) for _ in range(b_len))
    print('{} {} {}'.format(a, b, n))
    return (a, b, n)

def solve(a, b, n):
    full = ''
    last = a
    curr = b
    while True:
        full = last + curr
        last = curr
        curr = full
        if len(full) >= n:
            break
    print('Ans: {}'.format(full[n]))

# a, b, n = generate(100000, 100)
a, b, n = ("0782347791158056981510862750493378469071538466831568673837283604603446885327395358", "69", 13625)
solve(a, b, n)