import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import BayesianRidge

def show_causal_impact_bsts(df):
    st.title("📈 Bayesian Structural Time Series (Causal Impact)")

    store = st.selectbox(
        "Select Store",
        sorted(df["store_name"].unique())
    )

    store_df = df[df["store_name"] == store].copy()
    store_df.reset_index(drop=True, inplace=True)

    # -----------------------------
    # Intervention point
    # -----------------------------
    intervention_point = st.slider(
        "Intervention Start Index",
        min_value=10,
        max_value=len(store_df) - 10,
        value=int(len(store_df) * 0.6)
    )

    y = store_df["daily_revenue_inr"].values
    time = np.arange(len(y)).reshape(-1, 1)

    # -----------------------------
    # Pre-intervention training
    # -----------------------------
    X_pre = time[:intervention_point]
    y_pre = y[:intervention_point]

    model = BayesianRidge()
    model.fit(X_pre, y_pre)

    # -----------------------------
    # Counterfactual prediction
    # -----------------------------
    y_pred, y_std = model.predict(time, return_std=True)

    lower = y_pred - 1.96 * y_std
    upper = y_pred + 1.96 * y_std

    # -----------------------------
    # Causal effect
    # -----------------------------
    actual_post = y[intervention_point:]
    counter_post = y_pred[intervention_point:]
    impact = actual_post - counter_post
    avg_impact = impact.mean()

    # -----------------------------
    # Visualization
    # -----------------------------
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(y, label="Actual Revenue")
    ax.plot(y_pred, label="Counterfactual", linestyle="--")
    ax.fill_between(
        range(len(y)),
        lower,
        upper,
        alpha=0.2,
        label="95% Credible Interval"
    )
    ax.axvline(intervention_point, color="red", linestyle=":")
    ax.legend()
    st.pyplot(fig)

    # -----------------------------
    # Results
    # -----------------------------
    st.metric("Average Causal Impact (₹ / day)", f"{avg_impact:,.0f}")

    if avg_impact > 0:
        st.success("✅ Intervention caused revenue increase")
    else:
        st.error("❌ Intervention caused revenue drop")

    st.caption("""
    This analysis estimates what revenue would have been
    if the intervention never happened.
    """)

