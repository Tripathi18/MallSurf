import pandas as pd
import numpy as np

df = pd.read_csv("processed_data.csv")

# High-value derived features
df['revenue_per_visitor'] = df['daily_revenue_inr'] / (df['store_footfall'] + 1)
df['avg_bill_value'] = df['daily_revenue_inr'] / (df['transaction_count'] + 1)
df['footfall_log'] = np.log1p(df['store_footfall'])
df['weekend_revenue_boost'] = df['is_weekend'] * df['store_footfall']

# Category mean encoding
cat_mean = df.groupby('category')['daily_revenue_inr'].mean()
df['category_mean_revenue'] = df['category'].map(cat_mean)

# One-hot encode
df = pd.get_dummies(df, columns=['day_of_week'], drop_first=True)

df.to_csv("features.csv", index=False)
print("Advanced feature engineering done.")
