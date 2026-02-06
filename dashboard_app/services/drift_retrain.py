import streamlit as st
import numpy as np
from scipy.stats import ks_2samp
import datetime

def show_drift_retrain(df):
    st.title("🔄 Drift-Based Auto Retraining Monitor")

    store = st.selectbox(
        "Select Store",
        sorted(df["store_name"].unique())
    )

    revenue = df[df["store_name"] == store]["daily_revenue_inr"].values

    split = int(len(revenue) * 0.75)
    past, recent = revenue[:split], revenue[split:]

    stat, p_value = ks_2samp(past, recent)

    st.metric("Drift p-value", f"{p_value:.5f}")

    retrain = False

    if p_value < 0.05:
        retrain = True
        st.error("🔴 Severe Drift Detected")
    elif p_value < 0.1:
        st.warning("🟠 Moderate Drift Detected")
    else:
        st.success("🟢 No Drift")

    # -----------------------------
    # Auto-Retrain Logic
    # -----------------------------
    st.subheader("🔧 Retraining Decision")

    if retrain:
        st.markdown("""
        **Recommended Actions:**
        - Retrain revenue model
        - Recalculate SHAP explanations
        - Refresh thresholds
        """)

        if st.button("🚀 Trigger Retraining"):
            with open("retrain_log.txt", "a") as f:
                f.write(f"Retrain triggered at {datetime.datetime.now()}\n")

            st.success("Retraining flag raised (safe mode)")
    else:
        st.info("Model performance stable")

