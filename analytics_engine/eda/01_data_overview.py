import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/MallSurf_Dataset_for_Analytics.csv")

df['record_date'] = pd.to_datetime(df['record_date'])

print("Shape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nDescribe:")
print(df.describe())

plt.hist(df['daily_revenue_inr'], bins=30)
plt.title("Daily Revenue Distribution")
plt.xlabel("Revenue (INR)")
plt.ylabel("Frequency")
plt.show()

plt.hist(df['store_footfall'], bins=30)
plt.title("Store Footfall Distribution")
plt.xlabel("Footfall")
plt.ylabel("Frequency")
plt.show()
