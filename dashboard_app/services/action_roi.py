import streamlit as st

def show_action_roi(base_revenue):
    st.subheader("📊 Action Cost vs Impact")

    actions = [
        ("Targeted Marketing Campaign", 50000, 0.08),
        ("Flash Sale / Discounts", 30000, 0.06),
        ("Store Layout Optimization", 20000, 0.04),
    ]

    for name, cost, uplift in actions:
        expected_gain = base_revenue * uplift
        impact_score = expected_gain / cost

        st.markdown(f"""
        **{name}**
        - 💸 Cost: ₹{cost:,}
        - 📈 Expected Revenue Gain: ₹{int(expected_gain):,}
        - ⚖️ Impact Score: **{impact_score:.2f}**
        """)

        if impact_score >= 2:
            st.success("🔥 High ROI – Recommended")
        elif impact_score >= 1:
            st.warning("⚠️ Medium ROI")
        else:
            st.info("🧊 Low ROI")
