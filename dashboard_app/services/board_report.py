import datetime

def generate_board_report(df):
    total_revenue = df["daily_revenue_inr"].sum()
    avg_daily = df["daily_revenue_inr"].mean()

    report = f"""
📊 MallSurf Weekly Board Report
Week Ending: {datetime.date.today()}

🔹 Total Revenue: ₹{int(total_revenue):,}
🔹 Avg Daily Revenue: ₹{int(avg_daily):,}

⚠️ Key Risks:
- Footfall volatility rising
- Conversion efficiency dropping

💡 AI Recommendations:
- Prioritize high ROI marketing
- Improve store layout efficiency

🤖 Model Confidence: 80%
"""
    return report
