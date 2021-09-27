#Oppgave 1b MAT-INF1100
import numpy as np
from math import sqrt

N = 100
x = np.zeros(N+3) # Liste med 103 null'er
x0 = 1 #initalbestingelse nr 1
x1 = 2 #initalbestingelse nr 2
x[0] = x0
x[1] = 2 - sqrt(5)

for N in range(0, N+1):
    x[N+2] = (4 * x[N+1]) + (x[N]) # formel som representerer n'te term
    print(f"{x[N]: g} n: {N}")
"""
Output
1          n: 0
-0.236068  n: 1
 0.0557281 n: 2
-0.0131556 n: 3
.
.
.
.
-1.20719e+46 n: 100
"""