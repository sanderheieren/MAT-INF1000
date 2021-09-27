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

"""
SIMULERT LØSNING:

1           n: 0
-0.236068   n: 1
 0.0557281  n: 2
-0.0131556  n: 3
 0.00310562 n: 4
.
.
.
.
-3.74908e+43 n: 96
-1.58813e+44 n: 97
-6.72745e+44 n: 98
-2.84979e+45 n: 99
-1.20719e+46 n: 100


ANALYTISK:

 1 n:0
-0.236068 n:1
 0.0557281 n:2
-0.0131556 n:3
 0.00310562 n:4
.
.
.
.
 6.47977e-61 n:96
-1.52967e-61 n:97
 3.61105e-62 n:98
-8.52454e-63 n:99
 2.01237e-63 n:100

"""