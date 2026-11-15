def create_alerts(feature_psi, prediction_psi, quality, performance=None):
    alerts = []
    if not quality.get("passed", False):
        alerts.append({"severity":"High","type":"Data quality","message":"Data quality checks failed."})
    for feature, value in feature_psi.items():
        if value is not None and value >= 0.25:
            alerts.append({"severity":"High","type":"Feature drift","message":f"High PSI detected for {feature}: {value:.3f}"})
        elif value is not None and value >= 0.10:
            alerts.append({"severity":"Medium","type":"Feature drift","message":f"Moderate PSI detected for {feature}: {value:.3f}"})
    if prediction_psi is not None and prediction_psi >= 0.25:
        alerts.append({"severity":"High","type":"Prediction drift","message":f"High prediction PSI: {prediction_psi:.3f}"})
    elif prediction_psi is not None and prediction_psi >= 0.10:
        alerts.append({"severity":"Medium","type":"Prediction drift","message":f"Moderate prediction PSI: {prediction_psi:.3f}"})
    if performance and performance.get("roc_auc") is not None and performance["roc_auc"] < 0.60:
        alerts.append({"severity":"High","type":"Performance","message":"ROC-AUC is below the illustrative 0.60 review threshold."})
    if not alerts:
        alerts.append({"severity":"Low","type":"Monitoring status","message":"No configured alert thresholds were breached."})
    return alerts
