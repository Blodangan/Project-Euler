#!/usr/bin/env python3

# Project Euler : Problem 1
# Multiples of 3 and 5

s = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        s += i

print(s)

# Solution : 233168

# Mathématiquement :
# La somme des multiples de n strictement inférieurs à N est simplement :
# n * somme pour k = 0 à k = m de k,
# avec m = le nombre entier strictement inférieur à N / n = ceil(N / n) - 1
# qui peut être simplifié par :
# n * m * (m + 1) / 2 , avec m = ceil(N / n) - 1
# Pour n = 3 et N = 1000, on a m = 333 donc :
# 3 * 333 * 334 / 2 = 166833
# Pour n = 5 et N = 1000, on a m = 199 donc :
# 5 * 199 * 200 / 2 = 99500
# Il faut prendre en compte qu'il existe des nombres que l'on compte deux fois
# si l'on somme ces résultats, les multiples de 15. Il suffit donc de les
# soustraire.
# Pour n = 15 et N = 1000, on a m = 66 donc :
# 15 * 66 * 67 / 2 = 33165
# Le résultat final étant :
# 166833 + 99500 - 33165 = 233168
