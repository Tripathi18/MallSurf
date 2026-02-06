import pandas as pd

df = pd.read_csv("../data/MallSurf_Dataset_for_Analytics.csv")

df['record_date'] = pd.to_datetime(df['record_date'])
df['day_of_week'] = df['day_of_week'].astype('category')
df['category'] = df['category'].astype('category')

df.to_csv("processed_data.csv", index=False)
print("Preprocessing done.")
