from pathlib import Path
import json
import pandas as pd
import streamlit as st

st.set_page_config(page_title="AIGuard", page_icon="🛡️", layout="wide")
st.title("AIGuard")
st.caption("Enterprise AI Governance, Model Drift Detection and Explainability Monitoring")
p=Path("data/processed/monitoring_report.json")
if not p.exists():
    st.warning("Run `python scripts/run_monitoring.py` to generate the monitoring report.")
    st.stop()
r=json.loads(p.read_text())
a,b,c,d=st.columns(4)
a.metric("Reference rows",r["reference_rows"])
b.metric("Current rows",r["current_rows"])
c.metric("Prediction PSI",f'{r["prediction_psi"]:.3f}')
d.metric("Active alerts",len([x for x in r["alerts"] if x["severity"]!="Low"]))
t1,t2,t3=st.tabs(["Drift", "Model Health", "Governance Alerts"])
with t1:
    st.subheader("Feature drift (PSI)")
    st.bar_chart(pd.Series(r["feature_psi"],name="PSI"))
with t2:
    st.subheader("Performance metrics")
    st.json(r["performance"])
    st.subheader("Feature importance snapshot")
    st.bar_chart(pd.Series(r["feature_importance"]))
with t3:
    st.subheader("Monitoring alerts")
    st.dataframe(pd.DataFrame(r["alerts"]),use_container_width=True)
    st.write("**Data quality passed:**",r["quality"]["passed"])
st.caption("Synthetic monitoring demonstration. Alerts are heuristics, not compliance findings.")
