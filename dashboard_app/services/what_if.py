import streamlit as st
import joblib
import os
import pandas as pd

def show_what_if(df, role):
    model_path = os.path.join(os.path.dirname(__file__), "../../analytics_engine/ml/best_model.pkl")
    model = joblib.load(model_path)

    st.markdown(f"### 🎛️ {role} Revenue Workspace")
    
    # --------------------------------------------------
    # 🎯 PERSONA-BASED SLIDERS
    # --------------------------------------------------
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if role == "Investor":
            footfall = st.slider("Global Portfolio Footfall", 5000, 50000, 12000)
            transactions = st.slider("Market Transaction Index", 1000, 20000, 3000)
        else:
            footfall = st.slider("Daily Store Traffic", 100, 5000, 1200)
            transactions = st.slider("Checkout Volume", 50, 2000, 300)
            
    with col2:
        sales_sqft = st.slider("Sales Density (per Sqft)", 0.5, 20.0, 5.0)
        st.info(f"Simulating high-impact levers for **{role}** objectives.")

    X = pd.DataFrame([{
        "store_footfall": footfall,
        "transaction_count": transactions,
        "sales_per_sqft": sales_sqft
    }])

    pred = model.predict(X)[0]

    st.markdown("<br>", unsafe_allow_html=True)
    st.metric(f"Projected {role} Outturn (₹)", f"{int(pred):,}")
    st.success("AI-driven scenario modeling complete.")
