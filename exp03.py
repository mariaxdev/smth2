data = input("Enter data bits: ")

m = len(data)
r = 0

while (2 ** r) < (m + r + 1):
    r += 1

n = m + r
code = ['0'] * (n + 1)

# Place data bits
j = 0
for i in range(1, n + 1):
    if i & (i - 1):       # Not a power of 2
        code[i] = data[j]
        j += 1

# Calculate parity bits
for p in range(r):
    pos = 2 ** p
    parity = 0
    for i in range(1, n + 1):
        if i & pos:
            parity ^= int(code[i])
    code[pos] = str(parity)

hamming = ''.join(code[1:])
print("Hamming Code:", hamming)

received = input("Enter received code: ")

# Error detection
error = 0
for p in range(r):
    pos = 2 ** p
    parity = 0
    for i in range(1, n + 1):
        if i & pos:
            parity ^= int(received[i - 1])
    if parity:
        error += pos

if error == 0:
    print("No error detected.")
else:
    print("Error detected at position:", error)

    # Correct the error
    received = list(received)
    received[error - 1] = '1' if received[error - 1] == '0' else '0'

    print("Corrected code:", ''.join(received))


# Sample Input:
# Enter data bits: 1011
# Enter received code: 0110011

# To test error correction:
# Change one bit in 0110011, for example:
# Enter received code: 0110001