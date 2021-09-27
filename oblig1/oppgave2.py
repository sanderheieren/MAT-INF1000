n = 100000
i = 99940
bin_co = 1 #startverdi for binomialkoeffisienten

for j in range(1, i + 1):
    bin_co = ((n - j + 1)/j) * bin_co
print(bin_co) 

"""
Output: python oppgave2.py

i) 26010428123750.0

ii) 2.702882409454359e+299

iii) inf
"""