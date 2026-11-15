from pathlib import Path
import json, joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from .data import load_batch, FEATURES
from .quality import quality_report
from .drift import psi_report, _psi
from .performance import performance_report
from .explainability import importance_snapshot
from .governance import create_alerts

def run_monitoring(reference_path="data/sample/reference_data.csv",
                   current_path="data/sample/current_data.csv"):
    ref, cur = load_batch(reference_path), load_batch(current_path)
    quality = quality_report(cur)
    model = Pipeline([("imputer", SimpleImputer(strategy="median")),
                      ("model", RandomForestClassifier(n_estimators=150, random_state=42,
                                                       class_weight="balanced"))])
    Xr, yr = ref[FEATURES], ref.target.astype(int)
    X_train, X_test, y_train, y_test = train_test_split(
        Xr, yr, test_size=0.25, random_state=42, stratify=yr
    )
    model.fit(X_train, y_train)
    p_ref = model.predict_proba(Xr)[:, 1]
    p_cur = model.predict_proba(cur[FEATURES])[:, 1]
    feature_psi = psi_report(ref, cur, FEATURES)
    prediction_psi = _psi(p_ref, p_cur)
    # Labels are available in this synthetic example; production labels may arrive later.
    performance = performance_report(cur.target.astype(int), p_cur)
    importance = importance_snapshot(model, FEATURES)
    alerts = create_alerts(feature_psi, prediction_psi, quality, performance)
    report = {
        "model_id":"demo-risk-model", "model_version":"1.0.0",
        "reference_rows":int(len(ref)), "current_rows":int(len(cur)),
        "quality":quality, "feature_psi":feature_psi,
        "prediction_psi":prediction_psi, "performance":performance,
        "feature_importance":importance, "alerts":alerts
    }
    Path("artifacts").mkdir(exist_ok=True)
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    joblib.dump(model, "artifacts/demo_model.joblib")
    Path("data/processed/monitoring_report.json").write_text(json.dumps(report, indent=2))
    cur.assign(prediction=p_cur).to_csv("data/processed/current_scored.csv", index=False)
    return report
