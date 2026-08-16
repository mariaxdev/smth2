import numpy as np
import matplotlib.pyplot as plt

f = float(input("Enter signal frequency: "))
fs = int(input("Enter sampling frequency: "))
n = int(input("Enter quantization levels: "))

t = np.arange(0, 1, 1/fs)
x = np.sin(2 * np.pi * f * t)

q = np.round((x + 1) * (n - 1) / 2)
pcm = ((q * 2 / (n - 1)) - 1)

print("PCM values:")
print(q.astype(int))

plt.plot(t, x, label="Original")
plt.step(t, pcm, label="Demodulated")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.show()