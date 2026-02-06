import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/MallSurf_Dataset_for_Analytics.csv")

plt.scatter(df['store_footfall'], df['transaction_count'], alpha=0.5)
plt.xlabel("Footfall")
plt.ylabel("Transactions")
plt.title("Footfall vs Transactions")
plt.show()

df['conversion_rate'].hist(bins=30)
plt.title("Conversion Rate Distribution")
plt.xlabel("Conversion Rate")
plt.show()

df.boxplot(column='conversion_rate', by='category', rot=45)
plt.title("Conversion Rate by Category")
plt.suptitle("")
plt.show()
