import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/MallSurf_Dataset_for_Analytics.csv")
df['record_date'] = pd.to_datetime(df['record_date'])

daily_rev = df.groupby('record_date')['daily_revenue_inr'].sum()
daily_rev.plot(figsize=(10,5), title="Total Mall Revenue Trend")
plt.ylabel("Revenue (INR)")
plt.show()

top_stores = df.groupby('store_name')['daily_revenue_inr'].sum().sort_values(ascending=False).head(10)
top_stores.plot(kind='bar', title="Top 10 Revenue Generating Stores")
plt.ylabel("Revenue (INR)")
plt.show()

cat_rev = df.groupby('category')['daily_revenue_inr'].sum()
cat_rev.plot(kind='pie', autopct='%1.1f%%', title="Revenue Share by Category")
plt.ylabel("")
plt.show()
