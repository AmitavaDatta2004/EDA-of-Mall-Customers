import pandas as pd

# Load Dataset
df = pd.read_csv('Mall_Customers.csv')

# Rename Genre to Gender for consistency
if 'Genre' in df.columns:
    df.rename(columns={'Genre': 'Gender'}, inplace=True)

# Display Info
print(f"Shape: {df.shape}")
print(f"Missing Values:\n{df.isnull().sum()}")

numerical_cols = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
for col in numerical_cols:
    print(f"{col} -> Mean: {df[col].mean():.2f}, Median: {df[col].median():.2f}, Mode: {df[col].mode()[0]}")


for col in numerical_cols:
    data_range = df[col].max() - df[col].min()
    var = df[col].var()
    std = df[col].std()
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    print(f"{col} -> Range: {data_range}, STD: {std:.2f}, IQR: {IQR}")

from scipy.stats import skew
for col in numerical_cols:
    s = skew(df[col])
    print(f"{col} Skewness: {s:.2f}")
    # Outlier logic (1.5 * IQR)

print(df['Gender'].value_counts())
print(df['Gender'].value_counts(normalize=True))