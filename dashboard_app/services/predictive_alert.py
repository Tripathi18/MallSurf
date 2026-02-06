import streamlit as st
import pandas as pd
import joblib
import os
import numpy as np

def show_predictive_alert(df):
    st.title("🚨 Predictive Alert: Revenue Risk Next Week")
    st.caption("AI-powered early warning system")

    # -------- Load model --------
    model_path = os.path.join(
        os.path.dirname(__file__),
        "../../analytics_engine/ml/best_model.pkl"
    )
    model = joblib.load(model_path)

    features = ['store_footfall', 'transaction_count', 'sales_per_sqft']

    store = st.selectbox("Select Store", df['store_name'].unique())
    store_df = df[df['store_name'] == store].copy()

    # -------- TIME HANDLING (ROBUST FIX) --------
    if 'date' in store_df.columns:
        store_df = store_df.sort_values('date')
        st.info("🗓️ Using date column for time ordering")
    else:
        store_df = store_df.reset_index(drop=True)
        store_df['time_index'] = range(len(store_df))
        #st.info("⏱️ Date column not found — using record order as time")

    if len(store_df) < 14:
        st.warning("Not enough historical data for prediction")
        return

    # -------- Baseline (last 7 records) --------
    last_week_actual = store_df['daily_revenue_inr'].tail(7).mean()

    # -------- Next-period prediction --------
    X_future = store_df[features].tail(7)
    future_preds = model.predict(X_future)
    next_week_pred = np.mean(future_preds)

    st.metric(
        "Predicted Avg Revenue (Next Period)",
        f"₹ {int(next_week_pred):,}"
    )

    # -------- Detect drop --------
    drop_pct = (last_week_actual - next_week_pred) / last_week_actual

    if drop_pct <= 0.05:
        st.success("✅ No major revenue drop expected in next period")
        return

    st.error(f"⚠️ Revenue Drop Risk Detected: {int(drop_pct * 100)}%")

    # -------- WHY ANALYSIS --------
    reasons = []

    if store_df['store_footfall'].tail(7).mean() < store_df['store_footfall'].iloc[-14:-7].mean():
        reasons.append("📉 Declining footfall trend")

    if store_df['transaction_count'].tail(7).mean() < store_df['transaction_count'].iloc[-14:-7].mean():
        reasons.append("🛒 Falling conversion efficiency")

    if store_df['sales_per_sqft'].tail(7).mean() < store_df['sales_per_sqft'].iloc[-14:-7].mean():
        reasons.append("📐 Reduced space efficiency")

    if not reasons:
        reasons.append("⚠️ External or seasonal demand slowdown")

    st.subheader("🔍 Why Revenue May Drop")
    for r in reasons:
        st.write("•", r)

    # -------- PREVENTIVE ACTIONS --------
    st.subheader("💡 Preventive Actions")

    action_shown = False

    for r in reasons:
        r_lower = r.lower()

        if "footfall" in r_lower:
            st.success("Increase mall events, local ads, or promotions to boost footfall")
            action_shown = True

        if "conversion" in r_lower or "transaction" in r_lower:
            st.success("Introduce limited-time offers and staff incentives to improve conversion")
            action_shown = True

        if "space" in r_lower or "sqft" in r_lower:
            st.success("Re-optimize store layout, product placement, and visual merchandising")
            action_shown = True

    if not action_shown:
        st.success("Monitor trends closely and prepare contingency promotions for demand slowdown")
