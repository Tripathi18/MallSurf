import streamlit as st

def get_user_role():
    return st.sidebar.selectbox(
        "Select Role",
        ["Investor", "Mall Manager", "Store Manager"]
    )
