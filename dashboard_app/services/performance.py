import streamlit as st
import plotly.express as px
from style import styled_metric

def show_performance(df, role):
    
    # --------------------------------------------------
    # 🎯 PERSONA-BASED ANALYSIS PATHWAY
    # --------------------------------------------------
    
    if role in ["Investor", "Mall Manager"]:
        # AGGREGATE VIEW: Store Ranking
        st.markdown('<p style="font-weight: 600; font-size: 1.2rem;">Store Performance Ranking</p>', unsafe_allow_html=True)
        
        # Calculate performance metrics per store
        shop_stats = df.groupby('store_name').agg({
            'daily_revenue_inr': 'sum',
            'conversion_rate': 'mean',
            'store_footfall': 'sum'
        }).reset_index().sort_values(by='daily_revenue_inr', ascending=False)

        col_l, col_r = st.columns([2, 1])

        with col_l:
            fig_rank = px.bar(
                shop_stats.head(10), 
                x='daily_revenue_inr', 
                y='store_name',
                orientation='h',
                color='daily_revenue_inr',
                color_continuous_scale='GnBu',
                labels={'daily_revenue_inr': 'Total Revenue (₹)', 'store_name': 'Store'}
            )
            fig_rank.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E0E0E0',
                margin=dict(t=0, b=0, l=0, r=0)
            )
            st.plotly_chart(fig_rank, use_container_width=True)

        with col_r:
            st.markdown('<p style="font-weight: 600; font-size: 1rem;">Top Velocity Stores</p>', unsafe_allow_html=True)
            for _, row in shop_stats.head(5).iterrows():
                st.markdown(f"""
                    <div style="background: rgba(255,255,255,0.03); padding: 10px; border-radius: 8px; margin-bottom: 5px; border-left: 3px solid #00F2FF;">
                        <span style="font-size: 0.9rem; font-weight: 600;">{row['store_name']}</span><br>
                        <span style="color: #00F2FF; font-size: 0.8rem;">₹{row['daily_revenue_inr']/1e3:.1f}K Revenue</span>
                    </div>
                """, unsafe_allow_html=True)

    else: # Store Manager (DEEP DIVE VIEW)
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown('<p style="font-weight: 600; font-size: 1.2rem;">Store Selection</p>', unsafe_allow_html=True)
            store = st.selectbox("Your Store", df['store_name'].unique(), label_visibility="collapsed")
            store_df = df[df['store_name'] == store]
            
            st.markdown("<br>", unsafe_allow_html=True)
            avg_rev = store_df['daily_revenue_inr'].mean()
            avg_conv = store_df['conversion_rate'].mean()
            
            styled_metric("Store Avg Day", f"₹{avg_rev:,.0f}", "+4.2%")
            styled_metric("Sales Conversion", f"{avg_conv*100:.1f}%", "-0.8%")

        with col2:
            st.markdown(f'<p style="font-weight: 600; font-size: 1.2rem;">{store} - Revenue Trajectory</p>', unsafe_allow_html=True)
            fig = px.area(
                store_df, 
                y='daily_revenue_inr',
                color_discrete_sequence=['#00F2FF']
            )
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#E0E0E0',
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="Revenue (₹)"),
                margin=dict(t=20, b=20, l=20, r=20)
            )
            st.plotly_chart(fig, use_container_width=True)
