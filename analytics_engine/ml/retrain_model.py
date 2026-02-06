import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("../data/MallSurf_Dataset_for_Analytics.csv")

X = df[['store_footfall', 'transaction_count', 'sales_per_sqft']]
y = df['daily_revenue_inr']

model = RandomForestRegressor(n_estimators=200)
model.fit(X, y)

joblib.dump(model, "best_model.pkl")
print("✅ Model retrained & updated")
