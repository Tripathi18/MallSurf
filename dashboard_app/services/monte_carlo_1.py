import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def show_monte_carlo(df, role):
    st.markdown(f"### 🎲 {role} Probabilistic Risk Profile")

    if role == "Investor":
        st.caption("Modeling asset volatility and downside CAPEX risks.")
        entity = "Portfolio Index"
    else:
        st.caption("Modeling operational revenue variance and store stability.")
        entity = "Store Outturn"

    store = st.selectbox("Entity for Simulation", sorted(df["store_name"].unique()))
    revenue = df[df["store_name"] == store]["daily_revenue_inr"]

    mean, std = revenue.mean(), revenue.std()
    simulations = st.slider("Monte Carlo Iterations", 1000, 10000, 5000)
    simulated = np.random.normal(mean, std, simulations)

    worst, best = np.percentile(simulated, 5), np.percentile(simulated, 95)

    # -----------------------------
    # 🎴 PERSONA-BASED METRICS
    # -----------------------------
    c1, c2, c3 = st.columns(3)
    if role == "Investor":
        c1.metric("Expected Yield", f"₹ {mean:,.0f}", "Stable")
        c2.metric("VAR (5% Downside)", f"₹ {worst:,.0f}", "-12%")
        c3.metric("95% Alpha Potential", f"₹ {best:,.0f}", "+15%")
    else:
        c1.metric("Predicted Daily Rev", f"₹ {mean:,.0f}", "Nominal")
        c2.metric("Critical Low (5%)", f"₹ {worst:,.0f}", "Action Required")
        c3.metric("Peak Target (95%)", f"₹ {best:,.0f}", "Achievement")

    # -----------------------------
    # 📈 DISTRIBUTION
    # -----------------------------
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)
    
    n, bins, patches = ax.hist(simulated, bins=80, alpha=0.7, color='#00C6FF')
    ax.axvline(mean, color='#00F2FF', linestyle="--", label="Expected Outcome", linewidth=2)
    ax.axvline(worst, color='#FF4B4B', linestyle=":", label="Risk Boundary", linewidth=2)
    
    plt.setp(ax.get_xticklabels(), color="#E0E0E0")
    plt.setp(ax.get_yticklabels(), color="#E0E0E0")
    ax.legend(facecolor=(0,0,0,0.5), edgecolor="white")
    st.pyplot(fig)

    # -----------------------------
    # 🧠 PERSONA INSIGHT
    # -----------------------------
    if role == "Investor":
        st.success("💎 **Strategic Insight**: The simulation shows a 95% confidence interval for asset maturity. Downside risk is manageable within current diversification limits.")
    elif role == "Mall Manager":
        st.success("⚡ **Ops Insight**: Operational consistency is high. Current variance suggests only a 5% probability of a significant revenue dip next week.")
    else: # Store Manager
        st.success("🛒 **Retail Insight**: Prepare for 'Worst Case' inventory stocking levels if current footfall volatility continues.")

