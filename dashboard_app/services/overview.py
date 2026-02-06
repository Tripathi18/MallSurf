import streamlit as st
import plotly.express as px
from style import styled_metric

def show_overview(df, role):
    
    # --------------------------------------------------
    # 🎯 PERSONA-BASED DATA AGGREGATION
    # --------------------------------------------------
    total_rev = df['daily_revenue_inr'].sum()
    avg_conv = df['conversion_rate'].mean()
    total_footfall = df['store_footfall'].sum()
    avg_spend = total_rev / total_footfall if total_footfall > 0 else 0

    # --------------------------------------------------
    # 🎴 KPI CARDS BY ROLE
    # --------------------------------------------------
    col1, col2, col3, col4 = st.columns(4)

    if role == "Investor":
        with col1:
            styled_metric("Portfolio Revenue", f"₹{total_rev/1e6:.2f}M", "+12.5%")
        with col2:
            styled_metric("Market Sentiment", "Bullish", "+0.4pt")
        with col3:
            styled_metric("Asset Footfall Index", f"{(total_footfall/1e6):.2f}M", "+5.4%")
        with col4:
            styled_metric("Yield (Est.)", "8.4%", "+1.2%")

    elif role == "Mall Manager":
        with col1:
            styled_metric("Gross Operational Rev", f"₹{total_rev/1e6:.2f}M", "+8.1%")
        with col2:
            styled_metric("Mall-wide Conversion", f"{avg_conv*100:.1f}%", "-1.2%")
        with col3:
            styled_metric("Daily Footfall Avg", f"{df['store_footfall'].mean():.0f}", "+3.2%")
        with col4:
            styled_metric("Occupancy Rate", "94%", "Stable")

    else: # Store Manager
        with col1:
            styled_metric("Net Sales Potential", f"₹{total_rev/1e6:.2f}M", "+15.2%")
        with col2:
            styled_metric("Store Conversion", f"{avg_conv*100:.1f}%", "+2.1%")
        with col3:
            styled_metric("Customer Traffic", f"{total_footfall/1e3:.1f}K", "+4.8%")
        with col4:
            styled_metric("Avg Transaction Value", f"₹{avg_spend:.0f}", "+0.5%")

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------
    # 📊 CHARTS BY ROLE
    # --------------------------------------------------
    col_left, col_right = st.columns([1, 1])

    with col_left:
        title = "Revenue Contribution by Category" if role != "Investor" else "Asset Class Allocation"
        st.markdown(f'<p style="font-weight: 600; font-size: 1.2rem;">{title}</p>', unsafe_allow_html=True)
        category_rev = df.groupby('category')['daily_revenue_inr'].sum().reset_index()
        fig_cat = px.pie(
            category_rev, 
            values='daily_revenue_inr', 
            names='category', 
            hole=0.4,
            color_discrete_sequence=['#00F2FF', '#00C6FF', '#0072FF', '#0044FF', '#0022AA']
        )
        fig_cat.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#E0E0E0',
            margin=dict(t=30, b=0, l=0, r=0),
            showlegend=True
        )
        st.plotly_chart(fig_cat, use_container_width=True)

    with col_right:
        trend_title = "Growth Velocity Index" if role == "Investor" else "Daily Performance Trend"
        st.markdown(f'<p style="font-weight: 600; font-size: 1.2rem;">{trend_title}</p>', unsafe_allow_html=True)
        daily_trend = df.groupby(df.index)['daily_revenue_inr'].sum().reset_index()
        fig_trend = px.area(
            daily_trend, 
            x=daily_trend.index, 
            y='daily_revenue_inr',
            color_discrete_sequence=['#00F2FF']
        )
        fig_trend.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#E0E0E0',
            xaxis=dict(showgrid=False, title="Time Horizon"),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="Metric Value (₹)"),
            margin=dict(t=20, b=20, l=20, r=20)
        )
        st.plotly_chart(fig_trend, use_container_width=True)
