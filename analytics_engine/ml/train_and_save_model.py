import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# ---------- PATHS ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "MallSurf_Dataset_for_Analytics.csv"
)

MODEL_PATH = os.path.join(BASE_DIR, "best_model.pkl")

# ---------- LOAD DATA ----------
df = pd.read_csv(DATA_PATH)

FEATURES = [
    'store_footfall',
    'transaction_count',
    'sales_per_sqft'
]

TARGET = 'daily_revenue_inr'

X = df[FEATURES]
y = df[TARGET]

# ---------- TRAIN ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# ---------- EVALUATE ----------
score = r2_score(y_test, model.predict(X_test))
print(f"Model R² Score: {round(score, 3)}")

# ---------- SAVE ----------
joblib.dump(model, MODEL_PATH)
print("✅ best_model.pkl saved at:", MODEL_PATH)
