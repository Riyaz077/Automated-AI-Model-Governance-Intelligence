from pathlib import Path
import json
from fastapi import FastAPI, HTTPException

app=FastAPI(title="AIGuard Governance Monitoring API",version="1.0.0",
 description="Demonstration endpoints for model monitoring summaries.")

@app.get("/")
def root():
    return {"service":"AIGuard","docs":"/docs"}

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/models")
def models():
    return [{"model_id":"demo-risk-model","version":"1.0.0","status":"monitored",
             "risk_tier":"demo"}]

@app.get("/monitoring/latest")
def latest():
    p=Path("data/processed/monitoring_report.json")
    if not p.exists():
        raise HTTPException(status_code=404,detail="Run monitoring pipeline first.")
    return json.loads(p.read_text())
