#!/usr/bin/env python3

# Project Euler : Problem 3
# Largest prime factor

from math import sqrt

# Plus grand premier diviseur de n
def PGPD(n):
    pMax = n
    div = 2
    while n != 1:
        if n % div == 0:
            pMax = div
            while n % div == 0:
                n /= div

        div += 1

    return pMax

print(PGPD(600851475143))

# Solution : 6857

# Notes :
# En utilisant la décomposition d'un nombre en facteurs premiers
# n = p_1^a_1 * p_2^a_2 * ... * p_m^a_m
# On remarque que le premier nombre qui divise n est son premier facteur
# premier, ici p_1.
# Ainsi, en divisant n, a_1 fois, on trouve :
# n' = p_2^a_2 * ... * p_m^a_m
# On réitère la methode jusqu'à ce que n possède la valeur 1 et alors,
# le dernier facteur trouvé est le plus grand facteur premier divisant n.
# Ici, on incrémente le diviseur testé par 1. On pourrait améliorer cela pour
# avoir un maximumm de nombres premiers. Une amélioration simple serait
# d'incrémenter de 2 à partir de div = 3
