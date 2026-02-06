import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("features.csv")
df = df.sort_values('record_date')

X = df.drop(['daily_revenue_inr', 'store_name', 'shop_id', 'record_date', 'category'], axis=1)
y = df['daily_revenue_inr']

split = int(0.8 * len(df))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = RandomForestRegressor(
    n_estimators=500,
    max_depth=18,
    min_samples_leaf=5,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)
pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, pred))
print("MAE:", mean_absolute_error(y_test, pred))
