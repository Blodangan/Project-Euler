#!/usr/bin/env python3

# Project Euler : Problem 10
# Summation of primes

from math import sqrt

primes = [2]
s = 2

i = 3
while primes[-1] < 2000000:
    isPrime = True
    for p in primes:
        if p > sqrt(i):
            break

        if i % p == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(i)
        s += i

    i += 2

s -= primes[-1]

print(s)

# Solution : 142913828922

# Notes :
# Même technique que le problème 7
