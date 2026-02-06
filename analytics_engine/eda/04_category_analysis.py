import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/MallSurf_Dataset_for_Analytics.csv")

cat_sqft = df.groupby('category')['sales_per_sqft'].mean().sort_values()
cat_sqft.plot(kind='barh', title="Average Sales per SqFt by Category")
plt.xlabel("Sales per SqFt")
plt.show()
