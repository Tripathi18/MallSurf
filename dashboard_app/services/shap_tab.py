import streamlit as st
import joblib
import shap
import os
import pandas as pd
import matplotlib.pyplot as plt

def show_shap(df, role):
    st.markdown(f"### 🧠 AI Explainability: {role} Insights")
    st.caption(f"Deconstructing the 'Why' behind performance from a {role} perspective.")

    model_path = os.path.join(os.path.dirname(__file__), "../../analytics_engine/ml/best_model.pkl")
    model = joblib.load(model_path)
    features = ['store_footfall', 'transaction_count', 'sales_per_sqft']

    col_sel, col_fig = st.columns([1, 2])

    with col_sel:
        explain_mode = st.radio("Resolution:", ["Store", "Category"], horizontal=False)
        if explain_mode == "Store":
            key = st.selectbox("Select Asset", df['store_name'].unique())
            subset = df[df['store_name'] == key]
        else:
            key = st.selectbox("Select Sector", df['category'].unique())
            subset = df[df['category'] == key]

    if len(subset) < 5:
        st.warning("Insufficient data for stable SHAP analysis")
        return

    X = subset[features]
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    with col_fig:
        fig, ax = plt.subplots(figsize=(8, 4))
        fig.patch.set_alpha(0)
        ax.patch.set_alpha(0)
        shap.summary_plot(shap_values, X, plot_type="bar", show=False)
        plt.setp(ax.get_xticklabels(), color="#E0E0E0")
        plt.setp(ax.get_yticklabels(), color="#E0E0E0")
        st.pyplot(fig)

    # --------------------------------------------------
    # 🎯 PERSONA-BASED INSIGHTS
    # --------------------------------------------------
    impact_df = pd.DataFrame({"feature": features, "impact": abs(shap_values).mean(axis=0)}).sort_values("impact", ascending=False)
    top_feature = impact_df.iloc[0]['feature']

    if role == "Investor":
        st.success(f"💎 **Yield Catalyst**: For {key}, the primary driver of asset appreciation is **{top_feature}**. Strategic focus should remain on optimizing this lever.")
    elif role == "Mall Manager":
        st.success(f"⚡ **Operational Lever**: AI indicates that {top_feature} is the linchpin for mall-wide efficiency in the {key} segment.")
    else: # Store Manager
        st.success(f"🛒 **Daily Driver**: To boost your store's sales, focus on **{top_feature}**. AI confirms this has the highest direct impact on your revenue.")
