#!/usr/bin/env python3

# Project Euler : Problem 5
# Smallest multiple

inc = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
n = inc

found = False
while not found:
    divisible = True
    for i in range(2, 21):
        if n % i != 0:
            divisible = False

    if divisible:
        found = True
    else:
        n += inc

print(n)

# Solution : 232792560

# Notes :
# Les nombres divisibles par n sont espacés de n : 0, n, 2 * n, 3 * n, ...
# Les nombres divisibles par des nombres premiers entre eux, n et m, sont
# espacés de n * m : 0, n * m, 2 * n * m, 3 * n * m, ...
# Donc en prenant le produit des nombres premiers entre 0 et 20 on est sur
# d'avoir une valeur d'incrément suffisante pour tomber sur le nombre
# recherché.

# Mathématiquement :
# 2 = 2^1
# 3 = 3^1
# 4 = 2^2
# 5 = 5^1
# 6 = 2^1 * 3^1
# 7 = 7^1
# 8 = 2^3
# 9 = 3^2
# 10 = 2^1 * 5^1
# 11 = 11^1
# 12 = 2^2 * 3^1
# 13 = 13^1
# 14 = 2^1 * 7^1
# 15 = 3^1 * 5^1
# 16 = 2^4
# 17 = 17^1
# 18 = 2^1 * 3^2
# 19 = 19^1
# 20 = 2^2 * 5^1
# On garde pour chaque nombre premier la plus grande puissance :
# 2^4, 3^2, 5^1, 7^1, 11^1, 13^1, 17^1, 19^1
# Et le résultat sera :
# 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232792560
