import numpy as np
import streamlit as st

def monte_carlo_simulation(base_revenue):
    st.subheader("🎲 What-If Revenue Simulator")

    simulations = np.random.normal(
        loc=base_revenue,
        scale=base_revenue * 0.15,
        size=1000
    )

    st.metric("Best Case", f"₹{int(np.percentile(simulations, 90)):,}")
    st.metric("Worst Case", f"₹{int(np.percentile(simulations, 10)):,}")
    st.metric("Most Likely", f"₹{int(simulations.mean()):,}")

