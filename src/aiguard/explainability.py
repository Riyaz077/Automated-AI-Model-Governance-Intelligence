def importance_snapshot(model, feature_names):
    """Extract global tree/linear importance where supported."""
    estimator = model
    if hasattr(model, "named_steps"):
        estimator = model.named_steps.get("model", model)
    if hasattr(estimator, "feature_importances_"):
        values = estimator.feature_importances_
    elif hasattr(estimator, "coef_"):
        values = abs(estimator.coef_[0])
    else:
        return {}
    return {str(k): float(v) for k, v in sorted(
        zip(feature_names, values), key=lambda item: item[1], reverse=True
    )}

def compare_importance(reference, current):
    keys = sorted(set(reference) | set(current))
    return {k: float(current.get(k, 0) - reference.get(k, 0)) for k in keys}
