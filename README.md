# AIGuard
## Enterprise AI Governance, Model Drift Detection and Explainability Monitoring Platform

AIGuard is an end-to-end AI model governance demonstrator designed to help teams register models, monitor prediction behaviour, detect data and performance drift, review explainability signals, and maintain an auditable model-monitoring workflow. It combines a Python monitoring pipeline, a Streamlit dashboard, and a FastAPI service.

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
## **Quick Start**

- Create and activate a Python virtual environment.
- Install the required project dependencies.
- Generate synthetic data using the data generation script.
- Execute the monitoring pipeline to perform data analysis and generate monitoring outputs.
- Launch the interactive Streamlit dashboard.
- Start the FastAPI backend for API-based access.
- Explore API endpoints through the Swagger documentation.
- Run automated tests using `pytest` to validate project functionality.

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

## **Limitations & Future Enhancements**

**Current Limitations**

- Relies on synthetic, batch-based tabular datasets.
- Uses Population Stability Index (PSI) for data drift detection.
- Implements a baseline classification model for monitoring.
- Provides basic feature-importance analysis rather than continuous explainability.

**Future Enhancements**

- Integrate model registries and automated monitoring schedules.
- Implement data validation rules and data contracts.
- Incorporate Evidently AI and WhyLabs monitoring frameworks.
- Introduce continuous model explainability using SHAP.
- Add fairness evaluation and bias monitoring metrics.
- Develop automated alert notifications and routing.
- Implement approval workflows for model updates.
- Enable secure, scalable, multi-tenant cloud deployment.

## PSI interpretation
The included example uses conventional illustrative PSI bands: below 0.10 (low shift), 0.10–0.25 (moderate shift), and above 0.25 (high shift). These are heuristics, not universal standards. Tune thresholds to the model, feature, sample size, and use case.

## Responsible governance
AIGuard is a prototype, not a certified governance or compliance product. It does not automatically establish compliance with any law, regulation, or framework. Production adoption requires documented controls, access management, audit retention, validation, human review, incident response, and domain-specific legal and risk assessment.

## Author

**Mohamed Riyaz S.**  
Integrated M.Tech, Computer Science and Engineering (Business Analytics)  
VIT Chennai
