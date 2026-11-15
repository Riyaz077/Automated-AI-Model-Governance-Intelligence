# AIGuard
## Enterprise AI Governance, Model Drift Detection and Explainability Monitoring Platform

AIGuard is an end-to-end AI model governance demonstrator designed to help teams register models, monitor prediction behaviour, detect data and performance drift, review explainability signals, and maintain an auditable model-monitoring workflow. It combines a Python monitoring pipeline, a Streamlit dashboard, and a FastAPI service.

> **Demo-data notice:** The included prediction and reference datasets are synthetic. Drift alerts and monitoring metrics demonstrate the workflow only; they are not evidence of production model degradation or regulatory compliance.

## Core capabilities
- Model registry with model metadata, owner, version, status, and risk tier.
- Data quality checks for missing values, schema consistency, and numeric ranges.
- Feature drift monitoring using Population Stability Index (PSI).
- Prediction drift monitoring through distribution comparisons.
- Delayed-label performance monitoring using accuracy, precision, recall, F1, and ROC-AUC.
- Explainability monitoring using feature-importance snapshots and change comparisons.
- Configurable alert severity and recommended governance actions.
- Streamlit dashboard for model inventory, monitoring runs, drift signals, and alert history.
- FastAPI endpoints for health, model inventory, and monitoring summaries.

## Architecture
```text
Reference Data + Current Production-Like Batch
                  |
                  v
         Data Quality Validation
                  |
          +-------+-------+
          |               |
          v               v
      Feature PSI     Prediction PSI
          |               |
          +-------+-------+
                  |
                  v
        Performance Monitoring
          (when labels arrive)
                  |
                  v
       Explainability Snapshot
                  |
                  v
       Alert & Governance Engine
                  |
           +------+------+
           |             |
           v             v
       Dashboard      REST API
```

## Technology stack
Python · Pandas · NumPy · Scikit-learn · Streamlit · FastAPI · Matplotlib · Joblib · Pytest

## Repository structure
```text
AIGuard/
├── api/main.py
├── config/config.yaml
├── dashboard/app.py
├── data/sample/
│   ├── reference_data.csv
│   └── current_data.csv
├── data/processed/.gitkeep
├── docs/                  # 20 governance and technical guides
├── notebooks/             # EDA, drift, performance, explainability
├── scripts/
│   ├── generate_data.py
│   └── run_monitoring.py
├── src/aiguard/
│   ├── data.py
│   ├── drift.py
│   ├── quality.py
│   ├── performance.py
│   ├── explainability.py
│   ├── governance.py
│   └── pipeline.py
├── tests/
├── .env.example
├── .gitignore
├── LICENSE
├── requirements.txt
└── pyproject.toml
```

## Quick start

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python scripts/generate_data.py
python scripts/run_monitoring.py
```

Launch the dashboard:
```bash
streamlit run dashboard/app.py
```

Launch the API:
```bash
uvicorn api.main:app --reload
```
API documentation: `http://127.0.0.1:8000/docs`

Run tests:
```bash
pytest -q
```

## Monitoring methodology
1. Load reference and current batches with a consistent feature schema.
2. Validate missingness, ranges, and schema compatibility.
3. Compare feature distributions using PSI.
4. Compare prediction distributions using PSI.
5. Evaluate predictive performance only when ground-truth labels are available.
6. Compare feature-importance snapshots as a basic explainability signal.
7. Convert monitoring results into severity levels and suggested review actions.
8. Save a timestamped monitoring report for dashboard and API consumption.

## Key concepts
- **Data drift:** Change in input feature distributions between a reference and current batch.
- **Prediction drift:** Change in the distribution of model outputs.
- **Performance degradation:** Change in predictive quality measured against subsequently available ground-truth labels.
- **Explainability monitoring:** Review of feature importance or local explanation behaviour over time. Importance changes do not by themselves prove model failure.
- **Governance:** Ownership, versioning, documentation, approval, monitoring, incident handling, and retirement.

## PSI interpretation
The included example uses conventional illustrative PSI bands: below 0.10 (low shift), 0.10–0.25 (moderate shift), and above 0.25 (high shift). These are heuristics, not universal standards. Tune thresholds to the model, feature, sample size, and use case.

## Responsible governance
AIGuard is a prototype, not a certified governance or compliance product. It does not automatically establish compliance with any law, regulation, or framework. Production adoption requires documented controls, access management, audit retention, validation, human review, incident response, and domain-specific legal and risk assessment.

## Limitations and roadmap
Current scope uses synthetic tabular batches, PSI-based drift checks, a simple baseline classifier, and feature-importance snapshots. Future work may add model registry integrations, scheduled monitoring, data contracts, Evidently/WhyLabs integrations, SHAP monitoring, fairness metrics, alert routing, approval workflows, and secure multi-tenant deployment.

## Author
**Mohamed Riyaz S.**  
Computer Science & Engineering | Business Analytics

## License
MIT. See `LICENSE`.
