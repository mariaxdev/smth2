data = input("Enter data bits: ")
gen = input("Enter generator bits: ")

r = len(gen) - 1
temp = list(data + "0" * r)

for i in range(len(data)):
    if temp[i] == "1":
        for j in range(len(gen)):
            temp[i + j] = str(int(temp[i + j]) ^ int(gen[j]))

crc = "".join(temp[-r:])
code = data + crc

print("CRC =", crc)
print("Transmitted code =", code)

received = input("Enter received code: ")
temp = list(received)

for i in range(len(received) - r):
    if temp[i] == "1":
        for j in range(len(gen)):
            temp[i + j] = str(int(temp[i + j]) ^ int(gen[j]))

if "1" in temp[-r:]:
    print("Error detected")
else:
    print("No error detected")