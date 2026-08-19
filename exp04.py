from scipy.stats import f_oneway, kruskal

group1 = [68, 72, 65, 70, 75, 71, 69, 74]
group2 = [78, 80, 76, 82, 79, 81, 77, 84]
group3 = [60, 64, 62, 65, 61, 63, 66, 67]

alpha = 0.05

f_stat, p_value = f_oneway(group1, group2, group3)

print("ONE-WAY ANOVA")
print("F-Statistic :", round(f_stat, 4))
print("P-Value :", round(p_value, 6))

if p_value < alpha:
    print("Decision : Reject Null Hypothesis")
    print("Conclusion : Significant difference exists among the groups.")
else:
    print("Decision : Fail to Reject Null Hypothesis")
    print("Conclusion : No significant difference among the groups.")

h_stat, p_value = kruskal(group1, group2, group3)

print("\nKRUSKAL-WALLIS TEST")
print("H-Statistic :", round(h_stat, 4))
print("P-Value :", round(p_value, 6))

if p_value < alpha:
    print("Decision : Reject Null Hypothesis")
    print("Conclusion : Significant difference exists among the groups.")
else:
    print("Decision : Fail to Reject Null Hypothesis")
    print("Conclusion : No significant difference among the groups.")