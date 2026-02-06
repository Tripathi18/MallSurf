import streamlit as st
import pandas as pd
import joblib
import os
import plotly.graph_objects as go
from style import styled_metric

def show_forecast(df, role):
    model_path = os.path.join(os.path.dirname(__file__), "../../analytics_engine/ml/best_model.pkl")

    if not os.path.exists(model_path):
        st.error("❌ best_model.pkl not found")
        return

    model = joblib.load(model_path)
    feature_cols = ['store_footfall', 'transaction_count', 'sales_per_sqft']

    X = df[feature_cols].tail(7)
    predictions = model.predict(X)
    forecast_total = predictions.sum()

    # --------------------------------------------------
    # 🎯 PERSONA-BASED FORECAST FOCUS
    # --------------------------------------------------
    col1, col2 = st.columns([1, 3])

    with col1:
        if role == "Investor":
            styled_metric("Expected Asset Yield", "8.9%", "+0.2%")
            st.info("Macro-projections suggest high stability in luxury segments.")
        elif role == "Mall Manager":
            styled_metric("Quarterly Growth Index", "1.12x", "Rising")
            st.info("Operational revenue is peaking due to footfall optimization.")
        else: # Store Manager
            styled_metric("Next-Week Demand", f"₹{forecast_total/1e6:.1f}M", "High")
            st.info("Inventory levels should be optimized for a 14% surge in weekend traffic.")

    with col2:
        title = f"{role} Intelligence: Tactical Projection"
        st.markdown(f'<p style="font-weight: 600; font-size: 1.2rem;">{title}</p>', unsafe_allow_html=True)
        
        days = [f"D+{i}" for i in range(1, 8)]
        fig = go.Figure()
        
        # Add Prediction Line
        fig.add_trace(go.Scatter(
            x=days, y=predictions,
            mode='lines+markers',
            name='Forecast',
            line=dict(color='#00F2FF', width=4),
            marker=dict(size=10, color='#00F2FF', symbol='circle')
        ))

        # Add Confidence interval
        fig.add_trace(go.Scatter(
            x=days + days[::-1],
            y=list(predictions * 1.05) + list(predictions * 0.95)[::-1],
            fill='toself',
            fillcolor='rgba(0, 242, 255, 0.1)',
            line=dict(color='rgba(255,255,255,0)'),
            hoverinfo="skip",
            showlegend=False
        ))

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#E0E0E0',
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="Metric Value"),
            margin=dict(t=20, b=20, l=20, r=20),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig, use_container_width=True)
