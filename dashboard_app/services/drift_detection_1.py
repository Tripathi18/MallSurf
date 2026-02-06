import streamlit as st
import numpy as np
from scipy.stats import ks_2samp

def show_drift_detection(df):
    st.title("🚨 Data Drift Detection")

    store = st.selectbox(
        "Select Store",
        sorted(df["store_name"].unique())
    )

    store_df = df[df["store_name"] == store]

    revenue = store_df["daily_revenue_inr"].values

    split = int(len(revenue) * 0.7)
    past = revenue[:split]
    recent = revenue[split:]

    stat, p_value = ks_2samp(past, recent)

    st.metric("Drift p-value", f"{p_value:.4f}")

    # -----------------------------
    # 🚨 DRIFT DECISION
    # -----------------------------
    if p_value < 0.05:
        st.error("🔴 DRIFT DETECTED – Business behavior changed")
        drift_level = "High"
    elif p_value < 0.1:
        st.warning("🟠 POSSIBLE DRIFT – Monitor closely")
        drift_level = "Medium"
    else:
        st.success("🟢 No drift detected")
        drift_level = "Low"

    # -----------------------------
    # 🧠 ACTIONS
    # -----------------------------
    st.subheader("Recommended Actions")

    if drift_level == "High":
        st.write("""
        - Retrain ML models
        - Re-evaluate promotions
        - Check footfall sources
        """)
    elif drift_level == "Medium":
        st.write("""
        - Increase monitoring
        - Run A/B tests
        """)
    else:
        st.write("No action needed")

