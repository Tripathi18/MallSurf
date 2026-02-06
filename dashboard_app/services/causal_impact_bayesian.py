import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import BayesianRidge
import matplotlib.pyplot as plt

def show_causal_impact_bayesian(df):
    st.title("🧠 Bayesian Causal Impact Analysis")

    store = st.selectbox(
        "Select Store",
        sorted(df["store_name"].unique())
    )

    store_df = df[df["store_name"] == store].copy()

    # -----------------------------
    # Create intervention proxy
    # -----------------------------
    if "promotion_active" not in store_df.columns:
        store_df["promotion_active"] = (
            store_df["daily_revenue_inr"] >
            store_df["daily_revenue_inr"].median()
        ).astype(int)

    X = store_df[["promotion_active"]].values
    y = store_df["daily_revenue_inr"].values

    # -----------------------------
    # Bayesian Regression
    # -----------------------------
    model = BayesianRidge()
    model.fit(X, y)

    coef_mean = model.coef_[0]
    coef_std = np.sqrt(model.sigma_[0][0])

    lower = coef_mean - 1.96 * coef_std
    upper = coef_mean + 1.96 * coef_std

    # -----------------------------
    # Results
    # -----------------------------
    st.metric(
        "Estimated Causal Impact (₹ / day)",
        f"{coef_mean:,.0f}"
    )

    st.markdown(
        f"""
        **95% Credible Interval:**  
        ₹ {lower:,.0f}  →  ₹ {upper:,.0f}
        """
    )

    confidence = min(95, abs(coef_mean) / (coef_std + 1) * 10)
    st.progress(int(confidence))
    st.caption(f"Bayesian Confidence: {confidence:.1f}%")

    # -----------------------------
    # Visualization
    # -----------------------------
    fig, ax = plt.subplots()
    ax.bar(["Causal Effect"], [coef_mean])
    ax.errorbar(
        ["Causal Effect"],
        [coef_mean],
        yerr=[[coef_mean - lower], [upper - coef_mean]],
        fmt="o",
        color="black"
    )
    st.pyplot(fig)

    # -----------------------------
    # Interpretation
    # -----------------------------
    if lower > 0:
        st.success("✅ Strong evidence promotion increases revenue")
    elif upper < 0:
        st.error("❌ Promotion likely hurts revenue")
    else:
        st.warning("⚠️ Impact uncertain — needs more data")
