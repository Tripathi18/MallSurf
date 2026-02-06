# services/predictive_alert_v2.py

import streamlit as st
import pandas as pd
import numpy as np

def show_predictive_alert_v2(df: pd.DataFrame):
    st.title("🚨 Predictive Revenue Alerts (Advanced)")

    # -----------------------------
    # SAFETY CHECKS
    # -----------------------------
    required_cols = ["store_name", "daily_revenue_inr"]
    for col in required_cols:
        if col not in df.columns:
            st.error(f"❌ Required column missing: {col}")
            return

    st.subheader("🔮 Revenue Risk Detection")

    store = st.selectbox(
        "Select Store",
        sorted(df["store_name"].unique())
    )

    store_df = df[df["store_name"] == store]

    avg_revenue = store_df["daily_revenue_inr"].mean()
    recent_revenue = store_df["daily_revenue_inr"].tail(7).mean()

    delta = ((recent_revenue - avg_revenue) / avg_revenue) * 100

    # -----------------------------
    # ALERT LOGIC
    # -----------------------------
    if delta < -10:
        level = "🔴 HIGH RISK"
        priority = "High"
    elif delta < -5:
        level = "🟠 MEDIUM RISK"
        priority = "Medium"
    else:
        level = "🟢 STABLE"
        priority = "Low"

    st.metric(
        "Revenue Change (%)",
        f"{delta:.2f}%",
        delta=f"{delta:.2f}%"
    )

    st.markdown(f"### Alert Level: **{level}**")
    st.markdown(f"### Action Priority: **{priority}**")

    # -----------------------------
    # CONFIDENCE SCORE
    # -----------------------------
    confidence = min(95, abs(delta) * 2 + 60)
    st.progress(int(confidence))
    st.caption(f"Alert Confidence: {confidence:.1f}%")

    # -----------------------------
    # PREVENTIVE ACTIONS
    # -----------------------------
    st.subheader("🛡️ Preventive Actions")

    if priority == "High":
        st.write("""
        - Increase mall footfall via events / discounts  
        - Run store-level promotions  
        - Improve visual merchandising  
        - Push WhatsApp / SMS offers
        """)
    elif priority == "Medium":
        st.write("""
        - Monitor daily KPIs  
        - Optimize staffing & inventory  
        - A/B test offers
        """)
    else:
        st.write("✅ No immediate action required")

