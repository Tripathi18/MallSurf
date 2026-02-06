import streamlit as st
import pandas as pd

def show_insights(df):
    st.title("📉 Revenue Drop Analysis (Auto Explanation)")
    st.caption("AI-driven root cause analysis")

    store = st.selectbox(
        "Select Store",
        df['store_name'].unique()
    )

    store_df = df[df['store_name'] == store].sort_values("date")

    if len(store_df) < 10:
        st.warning("Not enough data for trend analysis")
        return

    # ---------- Detect drop ----------
    recent_avg = store_df['daily_revenue_inr'].tail(3).mean()
    previous_avg = store_df['daily_revenue_inr'].iloc[-10:-3].mean()

    if recent_avg >= previous_avg:
        st.success("✅ No significant revenue drop detected.")
        return

    st.error("⚠️ Revenue Drop Detected")

    # ---------- Compare drivers ----------
    reasons = []

    if store_df['store_footfall'].tail(3).mean() < store_df['store_footfall'].iloc[-10:-3].mean():
        reasons.append("📉 Footfall decreased")

    if store_df['transaction_count'].tail(3).mean() < store_df['transaction_count'].iloc[-10:-3].mean():
        reasons.append("🛒 Fewer transactions (conversion issue)")

    if store_df['sales_per_sqft'].tail(3).mean() < store_df['sales_per_sqft'].iloc[-10:-3].mean():
        reasons.append("📐 Lower space efficiency")

    if len(reasons) == 0:
        reasons.append("⚠️ External or seasonal factors suspected")

    st.subheader("🔍 Likely Reasons")
    for r in reasons:
        st.write("-", r)

    # ---------- Recommendations ----------
    st.subheader("💡 AI Recommendations")

    if "Footfall decreased" in " ".join(reasons):
        st.success("Increase promotions or events to attract visitors")

    if "conversion" in " ".join(reasons).lower():
        st.success("Improve in-store offers or staff engagement")

    if "space" in " ".join(reasons).lower():
        st.success("Optimize layout or product placement")
