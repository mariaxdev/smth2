data = input("Enter data bits: ")
gen = input("Enter generator bits: ")

n = len(gen) - 1
temp = list(data + "0" * n)

for i in range(len(data)):
    if temp[i] == '1':
        for j in range(len(gen)):
            temp[i + j] = str(int(temp[i + j]) ^ int(gen[j]))

crc = ''.join(temp[-n:])
codeword = data + crc

print("CRC:", crc)
print("Transmitted data:", codeword)

received = input("Enter received data: ")
temp = list(received)

for i in range(len(received) - n):
    if temp[i] == '1':
        for j in range(len(gen)):
            temp[i + j] = str(int(temp[i + j]) ^ int(gen[j]))

remainder = ''.join(temp[-n:])

if '1' in remainder:
    print("Error detected!")
else:
    print("No error detected.")


# Sample Input:
# Enter data bits: 1101011011
# Enter generator bits: 10011
# Enter received data: 11010110111110