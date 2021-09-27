#Oppgave 1a obligatorisk oppgave MAT-INF1000
import numpy as np
from math import sqrt
N = 100
x = np.zeros(N+3) # Liste med 103 null'er
x0 = 1 #initalbestingelse nr 1
x1 = 2 #initalbestingelse nr 2
x[0] = x0
x[1] = x1

for N in range(0, N+1):
    x[N+2] = (4 * x[N+1]) + (x[N]) # formel som representerer n'te term
    print(f"{x[N]: g} n: {N}")

"""
1  n: 0
2  n: 1
9  n: 2
38 n: 3
.
.
.
.
 7.71632e+59 n: 96
 3.26869e+60 n: 97
 1.38464e+61 n: 98
 5.86542e+61 n: 99
 2.48463e+62 n: 100
"""