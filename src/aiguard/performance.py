from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def performance_report(y_true, probability, threshold=0.5):
    pred = (probability >= threshold).astype(int)
    result = {
        "accuracy": float(accuracy_score(y_true, pred)),
        "precision": float(precision_score(y_true, pred, zero_division=0)),
        "recall": float(recall_score(y_true, pred, zero_division=0)),
        "f1": float(f1_score(y_true, pred, zero_division=0))
    }
    result["roc_auc"] = float(roc_auc_score(y_true, probability)) if len(set(y_true)) > 1 else None
    return result
