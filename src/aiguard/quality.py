from .data import FEATURES

def quality_report(df):
    missing = {c: int(df[c].isna().sum()) for c in FEATURES}
    out_of_range = {
        "income": int((df.income < 0).sum()),
        "account_age_days": int((df.account_age_days < 0).sum()),
        "transaction_count": int((df.transaction_count < 0).sum()),
        "utilization": int(((df.utilization < 0) | (df.utilization > 1)).sum())
    }
    return {
        "row_count": int(len(df)),
        "missing_values": missing,
        "out_of_range": out_of_range,
        "passed": not any(missing.values()) and not any(out_of_range.values())
    }
