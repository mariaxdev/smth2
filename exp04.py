import heapq
import math
from collections import Counter

s = input("Enter a message: ")
freq = Counter(s)

heap = [[f, [[ch, ""]]] for ch, f in freq.items()]
heapq.heapify(heap)

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    for x in a[1:]:
        for y in x:
            y[1] = "0" + y[1]

    for x in b[1:]:
        for y in x:
            y[1] = "1" + y[1]

    heapq.heappush(heap, [a[0] + b[0]] + a[1:] + b[1:])

codes = {}
for x in heap[0][1:]:
    for ch, code in x:
        codes[ch] = code

h = 0
l = 0

for ch, f in freq.items():
    p = f / len(s)
    h -= p * math.log2(p)
    l += p * len(codes[ch])

print("Huffman Codes:")
for ch, code in codes.items():
    print(ch, ":", code)

print("Entropy =", h)
print("Average Length =", l)
print("Efficiency =", h / l * 100, "%")
print("Redundancy =", 100 - h / l * 100, "%")