import streamlit as st
import numpy as np

def detect_drift(old_data, new_data):
    old_mean = old_data.mean()
    new_mean = new_data.mean()

    drift_score = abs(new_mean - old_mean) / old_mean

    st.subheader("📉 Data Drift Detection")

    if drift_score > 0.15:
        st.error("⚠️ Significant drift detected")
        st.write(f"Drift Score: {drift_score:.2f}")
        st.write("🔁 Model retraining recommended")
    else:
        st.success("✅ No significant drift detected")
