from pathlib import Path
import pandas as pd

FEATURES = ["income", "account_age_days", "transaction_count",
            "avg_transaction_value", "utilization", "support_tickets"]

def load_batch(path):
    df = pd.read_csv(Path(path))
    missing = sorted(set(FEATURES + ["target"]) - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return df
