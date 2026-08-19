import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = 10
p = 0.5

x1 = np.arange(0, n + 1)
y1 = binom.pmf(x1, n, p)

plt.figure(figsize=(8, 5))
plt.bar(x1, y1)
plt.title("Binomial Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.show()

x2 = np.linspace(-4, 4, 1000)
y2 = norm.pdf(x2, 0, 1)

plt.figure(figsize=(8, 5))
plt.plot(x2, y2)
plt.title("Normal Distribution")
plt.xlabel("Random Variable")
plt.ylabel("Probability Density")
plt.grid()
plt.show()