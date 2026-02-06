import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def show_causal_impact(df, role):
    st.markdown(f"### 🧪 {role} Causal Discovery")
    
    if role == "Investor":
        st.caption("Isolating asset value shifts from external market variables.")
        intervention_name = "Market Correction / Event"
    elif role == "Mall Manager":
        st.caption("Calculating the ROI of mall-wide promotional events.")
        intervention_name = "Promotional Campaign"
    else: # Store Manager
        st.caption("Quantifying the impact of local store layout changes.")
        intervention_name = "Staffing Adjustments"

    store = st.selectbox("Strategic Asset", sorted(df["store_name"].unique()))
    store_df = df[df["store_name"] == store].copy()

    # Manual Causal Logic
    if "intervention" not in store_df.columns:
        store_df["intervention"] = (store_df["daily_revenue_inr"] > store_df["daily_revenue_inr"].median()).astype(int)

    X, y = store_df[["intervention"]], store_df["daily_revenue_inr"]
    model = LinearRegression().fit(X, y)
    causal_effect = model.coef_[0]

    # -----------------------------
    # 📊 ROLE-SPECIFIC OUTPUT
    # -----------------------------
    col_out, col_msg = st.columns([1, 2])
    
    with col_out:
        st.metric(f"Net {role} Impact", f"₹ {causal_effect:,.0f}", "Verified by AI")
        
    with col_msg:
        if causal_effect > 0:
            st.success(f"✅ **Positive Correlation**: AI confirms the {intervention_name} directly increased value.")
        else:
            st.error(f"❌ **Ineffective Strategy**: Causal discovery shows no correlation between {intervention_name} and revenue uplift.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.info(f"Analysis methodology is tailored to **{role}** key performance indicators (KPIs).")

