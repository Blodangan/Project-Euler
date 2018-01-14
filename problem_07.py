#!/usr/bin/env python3

# Project Euler : Problem 7
# 10001st prime

from math import sqrt

primes = [2]

i = 3
while len(primes) < 10001:
    isPrime = True
    for p in primes:
        if p > sqrt(i):
            break

        if i % p == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(i)

    i += 2

print(primes[-1])

# Solution : 104743

# Notes :
# L'idée est ici de garder dans une liste tous les nombres premiers
# rencontrés, cela permettant de vérifier si un nombre est divisble
# par l'un d'entre eux. Si ce n'est pas le cas, alors c'est un nombre
# premier et on peut l'ajouter à la liste.
#
# lst[-1] retourne le dernier élément d'une liste
