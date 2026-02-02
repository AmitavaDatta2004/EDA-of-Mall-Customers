import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy.stats import skew

# Ensure plots directory exists
os.makedirs('plots', exist_ok=True)

# Load Dataset
try:
    df = pd.read_csv('Mall_Customers.csv')
    # Rename Genre to Gender if present
    if 'Genre' in df.columns:
        df.rename(columns={'Genre': 'Gender'}, inplace=True)
    print("Dataset Loaded Successfully.")
except FileNotFoundError:
    print("Error: Mall_Customers.csv not found.")
    exit(1)

# Results file
results_file = open("results.txt", "w")

def log(message):
    print(message)
    results_file.write(message + "\n")

log("--- DATA UNDERSTANDING ---")
log(f"Shape: {df.shape}")
log(f"Columns: {list(df.columns)}")
log("\nData Types:")
log(str(df.dtypes))
log("\nMissing Values:")
log(str(df.isnull().sum()))

# Renaming for easier access if needed, but keeping original mostly
# Age, Annual Income (k$), Spending Score (1-100)
numerical_cols = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
categorical_cols = ['Gender']

log("\n--- MEASURES OF CENTRAL TENDENCY ---")
for col in numerical_cols:
    log(f"\nAttribute: {col}")
    log(f"Mean: {df[col].mean():.2f}")
    log(f"Median: {df[col].median():.2f}")
    mode_val = df[col].mode()[0]
    log(f"Mode: {mode_val}")

log("\n--- MEASURES OF DISPERSION ---")
for col in numerical_cols:
    log(f"\nAttribute: {col}")
    data_range = df[col].max() - df[col].min()
    log(f"Range: {data_range}")
    log(f"Variance: {df[col].var():.2f}")
    log(f"Standard Deviation: {df[col].std():.2f}")
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    log(f"IQR: {IQR:.2f}")

log("\n--- DISTRIBUTION ANALYSIS ---")
for col in numerical_cols:
    skewness = skew(df[col])
    log(f"\nAttribute: {col}")
    log(f"Skewness: {skewness:.2f}")
    if abs(skewness) < 0.5:
        log("Distribution: Approximately Symmetric")
    elif skewness > 0:
        log("Distribution: Positively Skewed")
    else:
        log("Distribution: Negatively Skewed")
    
    # Outlier detection using IQR
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
    if not outliers.empty:
        log(f"Potential Outliers count: {len(outliers)}")
        log(f"Outlier values: {outliers.values}")
    else:
        log("No significant outliers detected via IQR method.")

log("\n--- CATEGORICAL DATA ANALYSIS ---")
gender_counts = df['Gender'].value_counts()
gender_percentages = df['Gender'].value_counts(normalize=True) * 100
log("\nGender Distribution:")
log(str(gender_counts))
log("\nGender Percentage:")
log(str(gender_percentages))


# --- VISUALIZATION ---
sns.set(style="whitegrid")

# 1. Histograms
plt.figure(figsize=(15, 5))
for i, col in enumerate(numerical_cols, 1):
    plt.subplot(1, 3, i)
    sns.histplot(df[col], kde=True, bins=20, color='skyblue')
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.savefig('plots/histograms.png')
plt.close()

# 2. Box Plots
plt.figure(figsize=(15, 5))
for i, col in enumerate(numerical_cols, 1):
    plt.subplot(1, 3, i)
    sns.boxplot(y=df[col], color='lightgreen')
    plt.title(f'Box Plot of {col}')
plt.tight_layout()
plt.savefig('plots/boxplots.png')
plt.close()

# 3. Bar Chart (Gender)
plt.figure(figsize=(6, 5))
sns.countplot(x='Gender', data=df, palette='pastel')
plt.title('Gender Distribution')
plt.savefig('plots/gender_bar.png')
plt.close()

# 4. Scatter Plot (Income vs Score)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender', data=df, palette='viridis', s=60)
plt.title('Annual Income vs Spending Score')
plt.savefig('plots/scatter_income_score.png')
plt.close()

log("\n--- VISUALIZATIONS GENERATED ---")
log("Saved: histograms.png, boxplots.png, gender_bar.png, scatter_income_score.png")

results_file.close()
print("Analysis complete. Results saved to results.txt")
