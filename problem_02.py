#!/usr/bin/env python3

# Project Euler : Problem 2
# Even Fibonacci numbers

s = 0

u, v = 1, 2
while u < 4000000:
    if u % 2 == 0:
        s += u
    u, v = v, u + v

print(s)

# Solution : 4613732

# Notes :
# L'expression : a, b = c, d
# affecte à la variable a la valeur de c et à la variable b la valeur de d
# L'expression de droite est evaluée avant l'affectation.
# On peut par exemple échanger deux variables avec cette methode,
# sans passer par une variable temporaire :
# a, b = b, a
