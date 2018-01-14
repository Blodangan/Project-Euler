#!/usr/bin/env python3

# Project Euler : Problem 4
# Largest palindrome product

pMax = 0

for n in range(100, 1000):
    for m in range(100, n):
        p = n * m
        if p > pMax:
            s = str(n * m)
            if s == s[::-1]:
                pMax = p

print(pMax)

# Solution : 906609

# Notes :
# Comme n * m = m * n, on considère seulement les cas ou m <= n.
# On cherche a vérifier si le produit est un palindrome seulement si
# celui-ci est plus grand que le dernier palindrome trouvé.
# s[::-1] permet de renverser une chaine de caracteres. L'égalite s == s[::-1]
# permettant alors de vérifier si une chaine est un palindrome.
