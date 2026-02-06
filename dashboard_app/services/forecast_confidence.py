import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def show_forecast_confidence(actual, predictions):
    st.subheader("📈 Revenue Forecast with Confidence Bands")

    std = np.std(actual - predictions)

    upper = predictions + 1.96 * std
    lower = predictions - 1.96 * std

    fig, ax = plt.subplots()
    ax.plot(predictions, label="Forecast")
    ax.fill_between(range(len(predictions)), lower, upper, alpha=0.3)

    ax.legend()
    st.pyplot(fig)

    st.caption("95% Confidence Interval")
