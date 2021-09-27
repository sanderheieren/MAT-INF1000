#Oppgave 1d MAT-INF1100

import numpy as np
from math import sqrt

N = 100
x = np.zeros(N+3) # Liste med 103 null'er
x0 = 1 #initalbestingelse nr 1
x1 = 2 #initalbestingelse nr 2
x[0] = x0
x[1] = 2 - sqrt(5)

#Simulert løsning:
for N in range(0, N+1):
    x[N+2] = (4 * x[N+1]) + (x[N]) # formel som representerer n'te term
    print(f"{x[N]: g} n: {N}")

#Analytisk løsning:
for N in range(0, N+1):
    sum = (2 - sqrt(5))**N
    print(f"{sum: g} n:{N}")