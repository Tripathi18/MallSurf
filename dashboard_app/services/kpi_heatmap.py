import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_kpi_heatmap(df, role):
    st.markdown(f"### 🔥 {role} Spatial Intelligence Heatmap")
    
    # --------------------------------------------------
    # 🎯 PERSONA-BASED METRIC SELECTION
    # --------------------------------------------------
    if role == "Investor":
        metric = "daily_revenue_inr"
        cmap = "YlGnBu"
        label = "Revenue Yield (₹)"
    elif role == "Mall Manager":
        metric = "store_footfall"
        cmap = "OrRd"
        label = "Traffic Flow (Visitors)"
    else: # Store Manager
        metric = "conversion_rate"
        cmap = "Purples"
        label = "Conversion Intensity (%)"

    pivot = df.pivot_table(
        index="store_name",
        columns="category",
        values=metric,
        aggfunc="mean"
    )

    fig, ax = plt.subplots(figsize=(12, 8))
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)
    
    sns.heatmap(pivot, cmap=cmap, ax=ax, annot=True, fmt=".1f" if role != "Store Manager" else ".2%", 
                cbar_kws={'label': label})
    
    plt.setp(ax.get_xticklabels(), color="#E0E0E0", rotation=45)
    plt.setp(ax.get_yticklabels(), color="#E0E0E0")
    ax.set_xlabel("Sector", color="#E0E0E0")
    ax.set_ylabel("Asset Identity", color="#E0E0E0")
    
    st.pyplot(fig)
    st.info(f"Insight: Darker regions indicate peak **{label}** for your specific objective.")
