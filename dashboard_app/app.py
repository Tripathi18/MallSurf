import streamlit as st
import pandas as pd
import os
import sys

# --------------------------------------------------
# 🔧 PATH FIX
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# --------------------------------------------------
# 🎨 CUSTOM STYLE & UTILS
# --------------------------------------------------
from style import apply_custom_style, header_section

# --------------------------------------------------
# 📦 IMPORT SERVICES
# --------------------------------------------------
from services.auth import get_user_role
from services.overview import show_overview
from services.forecast import show_forecast
from services.performance import show_performance
from services.insights import show_insights
from services.predictive_alert_v2 import show_predictive_alert_v2

# --------------------------------------------------
# ⚙️ PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="MallSurf – Premium Intelligence",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Premium Styling
apply_custom_style()

# --------------------------------------------------
# 📊 LOAD DATA
# Paths are relative to this file for cloud compatibility
_current_dir = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(_current_dir, "..", "analytics_engine", "data", "MallSurf_Dataset_for_Analytics.csv")

@st.cache_data
def load_data():
    if not os.path.exists(DATA_PATH):
        # Return dummy data or stop if critical
        return None
    return pd.read_csv(DATA_PATH)

df = load_data()

if df is None:
    st.error("⚠️ **Deployment Alert**: Dataset not found in the expected path.")
    st.info("Please ensure the `analytics_engine/data/` folder is included in your repository.")
    st.stop()

# --------------------------------------------------
# 🧭 SIDEBAR - BRANDING & NAVIGATION
# --------------------------------------------------
with st.sidebar:
    st.markdown('<div class="sidebar-brand">🛍️ MallSurf AI</div>', unsafe_allow_html=True)
    
    st.markdown('<p style="text-align: center; color: #888888; font-size: 0.8rem;"><span class="status-pulse"></span>System Pulse: Optimal</p>', unsafe_allow_html=True)
    
    st.title("🧭 Navigation")
    page = st.radio(
        "Select Module",
        [
            "🏠 Overview",
            "📈 Store Performance",
            "🔮 Revenue Forecast",
            "🎯 Model Accuracy",
            "🧠 AI Explainability",
            "🎲 What-If Simulator",
            "🚨 Predictive Alerts",
            "💼 Investor Dashboard",
            "🔥 KPI Heatmap",
            "📉 Risk Analysis (Monte Carlo)",
            "📊 Causal Impact"
        ],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # 👤 User Context
    st.markdown("### 👤 User Context")
    role = get_user_role()
    st.info(f"Signed in as: **{role}**")

    st.divider()

    # 🤖 MALLSURF AI ASSISTANT (Premium Feature)
    st.markdown("### 🤖 MallSurf Copilot")
    with st.expander(f"💬 Chat as {role}", expanded=False):
        user_query = st.text_input("Ask about mall trends...", placeholder="e.g. 'Predict next month's footfall'")
        if user_query:
            st.write(f"🔍 *{role} AI is analyzing specific trends for you...*")
            
            # Simulated Role-Based Intelligence
            if role == "Investor":
                st.success("Analysis: Strategic growth remains strong at 4.5% YoY. Current asset allocation is optimized for low-risk yield.")
            elif role == "Mall Manager":
                st.success("Analysis: Footfall efficiency reached 88% today. Category mixing is optimal, but 'Luxury' shows slight drift.")
            else: # Store Manager
                st.success("Analysis: Your conversion potential is up 12%. Recommendation: Increase staff coverage between 4 PM - 7 PM.")

    # 🔮 REAL-TIME INTELLIGENCE FEED
    st.markdown("### 🔮 Intel Feed")
    
    intel_messages = {
        "Investor": [
            "Analyzing portfolio yield variances...",
            "Yield stability index: 94.2%",
            "Monitoring market risk boundaries...",
            "AI detected high-growth sector: Tech-Retail"
        ],
        "Mall Manager": [
            "Scanning mall-wide congestion spots...",
            "Operational efficiency peaking at 88%",
            "Cross-category conversion check: OK",
            "Footfall anomaly detected in North Wing"
        ],
        "Store Manager": [
            "Localizing demand-supply equilibrium...",
            "Conversion intensity up: 12%",
            "Optimizing staff schedule for peak...",
            "AI strategy: Upsell at checkout identified"
        ]
    }
    
    selected_msgs = intel_messages.get(role, ["Initializing Intelligence Engine..."])
    
    feed_html = '<div class="intel-feed">'
    for msg in selected_msgs:
        feed_html += f'<div class="intel-line"> > {msg}</div>'
    feed_html += '</div>'
    
    st.markdown(feed_html, unsafe_allow_html=True)

    st.divider()
    
    if st.button("📊 Send Board Report"):
        from services.board_report import generate_board_report
        from services.alert_email import send_email_alert
        report = generate_board_report(df)
        send_email_alert("📊 Weekly MallSurf Board Report", report)
        st.success("Board report sent!")

# --------------------------------------------------
# 🚦 ROUTING
# --------------------------------------------------

# Map clean names to selection
page_clean = page.split(" ", 1)[1] if " " in page else page

# --------------------------------------------------
# 🚦 ROUTING (Role-Aware)
# --------------------------------------------------

if page_clean == "Overview":
    header_section(f"{role} Intelligence – Executive Summary", "Tailored KPIs and strategic insights.")
    show_overview(df, role)

elif page_clean == "Store Performance":
    header_section("Performance Analysis", f"Role-specific deep dive for {role}.")
    show_performance(df, role)

elif page_clean == "Revenue Forecast":
    header_section("Predictive Forecasting", f"{role} focus: Revenue vs Operational outlook.")
    show_forecast(df, role)

elif page_clean == "Model Accuracy":
    header_section("Model Transparency", "Validation metrics for predictive engines.")
    from services.accuracy import show_accuracy
    show_accuracy(df, role)

elif page_clean == "AI Explainability":
    header_section("AI Trust & Explanations", "Understanding the 'Why' behind predictions.")
    from services.shap_tab import show_shap
    show_shap(df, role)

elif page_clean == "What-If Simulator":
    header_section("Scenario Planning", "Interactive simulation for strategic decisions.")
    from services.what_if import show_what_if
    show_what_if(df, role)

elif page_clean == "Predictive Alerts":
    header_section("Anomaly Intelligence", "Real-time AI-driven risk detection.")
    show_predictive_alert_v2(df)

elif page_clean == "Investor Dashboard":
    header_section("Investor Yield Hub", "Long-term growth and portfolio health.")
    from services.demo_mode import show_demo
    show_demo()

elif page_clean == "KPI Heatmap":
    header_section("Spatial Intelligence", "Visualizing performance density across the mall.")
    from services.kpi_heatmap import show_kpi_heatmap
    show_kpi_heatmap(df, role)

elif page_clean == "Risk Analysis (Monte Carlo)":
    header_section("Probabilistic Risk", "Simulating 10,000+ scenarios for revenue stability.")
    from services.monte_carlo_1 import show_monte_carlo
    show_monte_carlo(df, role)

elif page_clean == "Causal Impact":
    header_section("Strategic Attribution", "Isolating the true impact of specific interventions.")
    from services.causal_impact import show_causal_impact
    show_causal_impact(df, role)
