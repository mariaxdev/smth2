import math
from collections import Counter

s = input("Enter a message: ")
c = Counter(s)
n = len(s)
h = 0

for ch, f in c.items():
    p = f / n
    i = -math.log2(p)
    h += p * i
    print(ch, "P =", p, "Information =", i)

print("Entropy =", h, "bits/symbol")