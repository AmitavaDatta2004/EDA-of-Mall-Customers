# Exploratory Data Analysis of Mall Customers

## 1. Introduction
This report presents the findings from the Exploratory Data Analysis (EDA) of the Mall Customers dataset. The analysis aims to understand customer demographics and spending behavior to aid in data-driven marketing strategies.

## 2. Data Understanding
The dataset consists of **200 records** and **5 attributes**.
- **CustomerID**: Unique identifier (Integer)
- **Gender**: Categorical (Male/Female)
- **Age**: Numerical (Integer)
- **Annual Income (k$)**: Numerical (Integer)
- **Spending Score (1-100)**: Numerical (Integer)

There are **0 missing values** in the dataset.

## 3. Measures of Central Tendency
| Attribute | Mean | Median | Mode | Interpretation |
|---|---|---|---|---|
| **Age** | 38.85 | 36.00 | 32 | The average customer is around 39 years old. |
| **Annual Income (k$)** | 60.56 | 61.50 | 54 | Average income is ~$60.5k, indicating a middle-class customer base. |
| **Spending Score** | 50.20 | 50.00 | 42 | Spending score is balanced, centered around 50. |

## 4. Measures of Dispersion
| Attribute | Range | Variance | Std Dev | IQR | Interpretation |
|---|---|---|---|---|---|
| **Age** | 52 | 195.13 | 13.97 | 20.25 | Moderate spread in age. |
| **Annual Income (k$)** | 122 | 689.84 | 26.26 | 36.50 | High variation in income levels. |
| **Spending Score** | 98 | 666.85 | 25.82 | 38.25 | Wide variety of spending habits. |

## 5. Distribution Analysis & Outliers
- **Age**: Approximately Symmetric (Skewness: 0.48). No outliers.
- **Annual Income**: Approximately Symmetric (Skewness: 0.32). **2 Potential Outliers** detected (High Income > 130k).
- **Spending Score**: Approximately Symmetric (Skewness: -0.05). No outliers.

## 6. Categorical Analysis
### Gender Distribution
- **Female**: 112 (56.0%)
- **Male**: 88 (44.0%)

![Gender Distribution](plots/gender_bar.png)

## 7. Visualizations

### Histograms (Distributions)
![Histograms](plots/histograms.png)
*Age is slightly right-skewed, while Spending Score is normally distributed.*

### Box Plots (Outliers)
![Box Plots](plots/boxplots.png)
*Annual Income shows outliers on the higher end.*

### Scater Plot (Income vs Spending Score)
![Income vs Score](plots/scatter_income_score.png)
*Distinct clusters are visible, suggesting potential segments (e.g., High Income-High Spend, Low Income-High Spend).*

## 8. Business Insights & Implications
1.  **Female Dominance**: 56% of customers are female. Marketing campaigns should likely prioritize products appealing to women.
2.  **Prime Age Group**: With a mean age of ~39 and mode of 32, the target demographic is young to middle-aged adults.
3.  **Income disparity**: There is a wide range of incomes (up to 137k). Luxury items could be targeted at the high-income outliers and upper quartiles.
4.  **Spending Score Clusters**: The scatter plot reveals distinct groups. For example, there is a group of customers with low income but high spending scores—these might be brand loyalists or impulse buyers worth retaining.
5.  **Middle Class Core**: The median income is ~61.5k, suggesting the bulk of customers are middle class. Value-for-money promotions would be effective for this majority.
