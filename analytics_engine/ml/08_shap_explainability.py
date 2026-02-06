import shap
import pandas as pd
from xgboost import XGBRegressor

df = pd.read_csv("features.csv")

X = df.drop(
    ['daily_revenue_inr', 'store_name', 'shop_id', 'record_date', 'category'],
    axis=1
)
y = df['daily_revenue_inr']

model = XGBRegressor(n_estimators=300, random_state=42)
model.fit(X, y)

explainer = shap.Explainer(model)
shap_values = explainer(X)

shap.summary_plot(shap_values, X)
