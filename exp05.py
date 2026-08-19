import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, linregress

x = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([45, 50, 55, 60, 65, 70, 78, 85, 90])

correlation, p_value = pearsonr(x, y)

slope, intercept, r_value, p_value, std_err = linregress(x, y)

y_pred = slope * x + intercept

print("Correlation Coefficient:", round(correlation, 4))
print("P-Value:", round(p_value, 6))
print("Slope:", round(slope, 4))
print("Intercept:", round(intercept, 4))
print("Regression Equation: y =", round(slope, 4), "x +", round(intercept, 4))

plt.scatter(x, y)
plt.plot(x, y_pred)
plt.title("Correlation and Linear Regression")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid()
plt.show()