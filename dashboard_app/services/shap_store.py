import streamlit as st
import shap
import matplotlib.pyplot as plt
import numpy as np

def show_store_shap(model, X, store_name):
    st.subheader(f"🧠 SHAP Waterfall – {store_name}")

    explainer = shap.Explainer(model)
    shap_values = explainer(X)

    fig = plt.figure()
    shap.plots.waterfall(shap_values[0], show=False)
    st.pyplot(fig)
