import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Age": [18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    "Marks": [65, 72, 80, 68, 75, 85, 90, 78, 88, 92],
    "Study_Hours": [2, 3, 4, 2, 5, 6, 7, 4, 6, 8]
}

df = pd.DataFrame(data)

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

df.hist(figsize=(10, 6))
plt.suptitle("Distribution of Features")
plt.show()

plt.figure(figsize=(8, 5))
plt.imshow(df.corr(), cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.columns)), df.columns)
plt.title("Correlation Matrix")
plt.show()

for column in df.columns:
    plt.figure(figsize=(6, 4))
    plt.boxplot(df[column])
    plt.title("Boxplot of " + column)
    plt.ylabel(column)
    plt.show()