import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV

df = pd.read_csv("features.csv")

X = df.drop(['daily_revenue_inr', 'store_name', 'shop_id', 'record_date', 'category'], axis=1)
y = df['daily_revenue_inr']

param_grid = {
    'n_estimators': [300, 500, 700],
    'max_depth': [10, 15, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 3, 5]
}

rf = RandomForestRegressor(random_state=42, n_jobs=-1)

search = RandomizedSearchCV(
    rf,
    param_grid,
    n_iter=20,
    cv=3,
    scoring='r2',
    verbose=2
)

search.fit(X, y)

print("Best Params:", search.best_params_)
print("Best R2:", search.best_score_)
