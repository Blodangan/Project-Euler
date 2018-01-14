#!/usr/bin/env python3

# Project Euler : Problem 9
# Special Pythagorean triplet

from math import sqrt

a, b = 1, 2
p = 0

found = False
while not found:
    c = sqrt(a * a + b * b)
    cInt = int(c)

    if c == cInt and a + b + cInt == 1000:
        p = a * b * cInt
        found = True

    a += 1
    if b <= a:
        a = 1
        b += 1

print(p)

# Solution : 31875000

# Notes :
# Pour vérifier qu'un nombre x est un entier, on vérifie l'égalite entre
# sa partie entière int(x) et le nombre lui-même.
# Ligne 20-23 : La condition nous permet d'avoir un nombre a toujours
# inférieur au nombre b en incrémentant b d'une unité et en faisant
# repartir a au nombre 1.

# Mathématiquement :
# On peut décrire tous les triplets pythagoriciens (a, b, c) avec deux nombres
# n et m, (m > n) :
# a = m * n, b = (m^2 - n^2) / 2, c = (m^2 + n^2) / 2
# Leur somme est :
# a + b + c = m * n + m^2 = m * (n + m)
# Or 1000 = 2^3 * 5^3 = 25 * (15 + 25)
# Donc (m, n) = (25, 15)
# et, a = 375, b = 200, c = 425
# Le résultat est :
# a * b * c = 375 * 200 * 425 = 31875000
