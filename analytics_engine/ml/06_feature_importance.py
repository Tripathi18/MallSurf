import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("features.csv")

X = df.drop(['daily_revenue_inr', 'store_name', 'shop_id', 'record_date', 'category'], axis=1)
y = df['daily_revenue_inr']

model = RandomForestRegressor(n_estimators=300, random_state=42)
model.fit(X, y)

imp = pd.Series(model.feature_importances_, index=X.columns).sort_values()

imp.tail(10).plot(kind='barh', title="Top Revenue Drivers")
plt.show()
