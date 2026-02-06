import pandas as pd
from dashboard_app.services.board_report import generate_board_report
from dashboard_app.services.alert_email import send_email_alert

df = pd.read_csv("analytics_engine/data/MallSurf_Dataset_for_Analytics.csv")

report = generate_board_report(df)
send_email_alert("📊 Weekly MallSurf Board Report", report)
