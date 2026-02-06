import streamlit as st

def apply_custom_style():
    """Injects custom CSS for a premium glassmorphic dark theme."""
    st.markdown("""
        <style>
        /* Modern Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }

        /* Main App Background */
        .stApp {
            background: radial-gradient(circle at 10% 20%, rgb(0, 0, 0) 0%, rgb(15, 15, 30) 90.2%);
            color: #E0E0E0;
        }

        /* Glassmorphism Sidebar */
        [data-testid="stSidebar"] {
            background-color: rgba(20, 20, 35, 0.7);
            backdrop-filter: blur(15px);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Custom Metric Cards */
        .metric-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            margin-bottom: 20px;
        }

        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 255, 255, 0.1);
            border: 1px solid rgba(0, 255, 255, 0.3);
        }

        .metric-label {
            color: #888888;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 600;
        }

        .metric-value {
            color: #00F2FF;
            font-size: 1.8rem;
            font-weight: 700;
            margin: 5px 0;
        }

        /* Neon Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #00C6FF 0%, #0072FF 100%);
            color: white;
            border: none;
            padding: 10px 25px;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .stButton>button:hover {
            box-shadow: 0 0 15px rgba(0, 198, 255, 0.6);
            transform: scale(1.02);
        }

        /* Sidebar Branding */
        .sidebar-brand {
            font-size: 1.5rem;
            font-weight: 800;
            background: -webkit-linear-gradient(#00C6FF, #0072FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 30px;
            text-align: center;
        }

        /* Pulsing Status Indicator */
        .status-pulse {
            width: 10px;
            height: 10px;
            background: #00FF88;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
            box-shadow: 0 0 8px #00FF88;
            animation: pulse-animation 2s infinite;
        }

        @keyframes pulse-animation {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(0, 255, 136, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 136, 0); }
        }

        /* Glassmorphism sidebar hover */
        .st-emotion-cache-16idsys:hover {
            background-color: rgba(255, 255, 255, 0.05);
        }
        /* Intelligence Feed */
    .intel-feed {
        background: rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(0, 255, 136, 0.2);
        border-radius: 8px;
        padding: 10px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 0.75rem;
        color: #00FF88;
        max-height: 150px;
        overflow-y: auto;
        margin-top: 10px;
        border-left: 3px solid #00FF88;
    }
    
    .intel-line {
        margin-bottom: 5px;
        border-bottom: 1px solid rgba(0, 255, 136, 0.05);
    }
    </style>
    """, unsafe_allow_html=True)

def styled_metric(label, value, delta=None):
    """Custom styled metric card with HTML/CSS."""
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            {"<div style='color: #00FF88; font-size: 0.8rem;'>↑ " + delta + "</div>" if delta else ""}
        </div>
    """, unsafe_allow_html=True)

def header_section(title, subtitle):
    """Modern header section with gradient text."""
    st.markdown(f"""
        <div style="margin-bottom: 40px;">
            <h1 style="font-weight: 800; font-size: 2.5rem; margin-bottom: 5px;">{title}</h1>
            <p style="color: #888888; font-size: 1.1rem;">{subtitle}</p>
            <div style="height: 4px; width: 60px; background: linear-gradient(90deg, #00C6FF, #0072FF); border-radius: 2px; margin-top: 15px;"></div>
        </div>
    """, unsafe_allow_html=True)
