import numpy as np
from scipy.stats import f_oneway, chi2_contingency

group1 = [12, 15, 14, 10, 13]
group2 = [18, 20, 19, 17, 21]
group3 = [25, 23, 24, 26, 22]

f_stat, p_value = f_oneway(group1, group2, group3)

print("One-Way ANOVA")
print("F-statistic:", f_stat)
print("P-value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

observed = np.array([
    [30, 20],
    [10, 40]
])

chi_stat, chi_p, dof, expected = chi2_contingency(observed)

print("\nChi-Square Test")
print("Chi-square statistic:", chi_stat)
print("P-value:", chi_p)

if chi_p < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")