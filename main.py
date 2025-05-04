# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display the first few rows
print("First 5 rows:")
print(df.head())

# Explore structure
print("\nDataset info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Clean the dataset (none missing, but I'll show the method)
df = df.dropna()

# Task 2: Basic Data Analysis
print("\nDescriptive Statistics:")
print(df.describe())

# Group by species and calculate the mean
grouped = df.groupby("target").mean()
print("\nMean of numerical columns grouped by species (target):")
print(grouped)

# Map target numbers to species names
df['species'] = df['target'].map(dict(enumerate(iris.target_names)))

# Task 3: Data Visualization

# Set plot style
sns.set(style="whitegrid")

# 1. Line chart (simulate time series by using index)
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.plot(df.index, df['petal length (cm)'], label='Petal Length')
plt.title("Line Chart of Sepal and Petal Lengths")
plt.xlabel("Index (as pseudo-time)")
plt.ylabel("Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart - Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal length (cm)', data=df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram - Distribution of Sepal Width
plt.figure(figsize=(8, 5))
plt.hist(df['sepal width (cm)'], bins=15, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# Findings
print("\nObservations:")
print("- Iris virginica has the highest average petal length.")
print("- Sepal width shows a normal distribution.")
print("- There is a strong positive correlation between sepal length and petal length.")
print("- Each species forms distinct clusters in the scatter plot, useful for classification.")