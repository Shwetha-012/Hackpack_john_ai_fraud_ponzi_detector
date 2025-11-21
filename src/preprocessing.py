# preprocessing.py

def preprocess_data(investment, monthly_return, duration):
    """
    Prepare and structure the data from form inputs
    """
    data = {
        "initial_investment": float(investment),
        "return_rate": float(monthly_return),
        "duration": int(duration)
    }
    return data


def detect_ponzi(data):
    """
    Simple rule-based fraud detection
    """

    risk_score = 0

    return_rate = data["return_rate"]
    duration = data["duration"]

    if return_rate > 20:
        risk_score += 30
    if return_rate > 40:
        risk_score += 40
    if duration < 6:
        risk_score += 20

    if risk_score >= 70:
        return "HIGH RISK - Possible Ponzi Scheme 🚨"
    elif risk_score >= 40:
        return "MEDIUM RISK - Suspicious ⚠"
    else:
        return "LOW RISK - Probably Safe ✅"