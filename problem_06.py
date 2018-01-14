#!/usr/bin/env python3

# Project Euler : Problem 6
# Sum square difference

s = sSq = 0

for n in range(1, 101):
    s += n
    sSq += n * n

diff = s * s - sSq

print(diff)

# Solution : 25164150

# Mathématiquement :
# La somme au carré des n premiers nombres est :
# ( n * (n + 1) / 2 )^2
# Ici, elle vaut ( 100 * 101 / 2 )^2 = 25502500
# La somme des n premiers carrés est :
# n * (n + 1) * (2 * n + 1) / 6
# Ici, elle vaut 100 * 101 * 201 / 6 = 338350
# Donc le résultat est :
# 25502500 - 338350 = 25164150
