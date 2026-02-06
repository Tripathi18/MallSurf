import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/MallSurf_Dataset_for_Analytics.csv")

weekend = df[df['is_weekend'] == 1]
weekday = df[df['is_weekend'] == 0]

labels = ['Revenue', 'Footfall', 'Conversion']
weekend_vals = [
    weekend['daily_revenue_inr'].mean(),
    weekend['store_footfall'].mean(),
    weekend['conversion_rate'].mean()
]

weekday_vals = [
    weekday['daily_revenue_inr'].mean(),
    weekday['store_footfall'].mean(),
    weekday['conversion_rate'].mean()
]

x = range(len(labels))
plt.bar(x, weekend_vals, width=0.4, label='Weekend')
plt.bar([i+0.4 for i in x], weekday_vals, width=0.4, label='Weekday')
plt.xticks([i+0.2 for i in x], labels)
plt.legend()
plt.title("Weekend vs Weekday Performance")
plt.show()
