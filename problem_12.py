#!/usr/bin/env python3

# Project Euler : Problem 12
# Highly divisible triangular number

def divisors(n):
    div = 1
    d  = 2
    while n != 1:
        a = 0
        while n % d == 0:
            n /= d
            a += 1
        div *= a + 1
        d += 1

    return div

t = 1
inc = 2

while divisors(t) <= 500:
    t += inc
    inc += 1

print(t)

# Solution : 76576500
