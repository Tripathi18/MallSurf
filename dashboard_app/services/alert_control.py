def should_alert(priority, roi_score):
    if priority == "HIGH" and roi_score > 1.5:
        return True
    return False
