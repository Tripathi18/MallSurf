import os
from datetime import time

import joblib
import pandas as pd
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "analytics_engine",
    "ml",
    "best_model.pkl"
)

model = joblib.load(MODEL_PATH)

while True:
    try:
        r = requests.get("http://localhost:5000/latest", timeout=5)

        if r.status_code != 200 or not r.text.strip():
            print("⏳ No data yet...")
            time.sleep(3)
            continue

        rows = r.json()

        if not rows:
            print("⏳ Waiting for POS data...")
            time.sleep(3)
            continue

        df = pd.DataFrame(rows)

        preds = model.predict(df[["footfall", "avg_bill"]])
        df["predicted_revenue"] = preds

        print("✅ Prediction OK:", preds.mean())

    except Exception as e:
        print("⚠️ Streaming error:", e)

    time.sleep(5)