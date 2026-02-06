import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/MallSurf_Dataset_for_Analytics.csv")

top20 = df.groupby('store_name')['daily_revenue_inr'].sum().sort_values(ascending=False)
share = top20.head(int(0.2 * len(top20))).sum() / top20.sum() * 100

print(f"Top 20% stores contribute {share:.2f}% of revenue")

df.groupby('category')['sales_per_sqft'].mean().plot(kind='bar', title="Sales per SqFt by Category")
plt.show()
